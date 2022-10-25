# pylint: disable=E0110
# pylint: disable=E1121
# pylint: disable=E0611
 

from utils.utilsFuncionts import *
from bs4 import BeautifulSoup
from time import sleep
import sys
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from startup.startup import dataFalseTemplate, dataTrueTemplate, requisitesList

def computeRequisites(url, dataTrue, dataFalse, requisites ):
    initializeDict(dataTrue)
    initializeDict(dataFalse)
    browser.get(url + "transparencia")
    sleep(0.3) 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    accordionItems = soup.select(".accordion-item-text")

    print("Obteniendo los requisitos de: ", url)
    for requisite in tqdm(requisites):
        flagExistence = False
        for item in  accordionItems:
            if wordExists(requisite.keyword, item):
                flagExistence = True
                link = item.select_one("a").get("href")
                if ("http") in link:
                    hrefLink = link
                    flagExternal = True
                else:
                    hrefLink = url+link
                    flagExternal = False
                browser.get(hrefLink)
                sleep(0.3)
                
                childSoup = BeautifulSoup(browser.page_source, "html.parser")
                onPage, date, title, info, address = requisite.checkRequisites(childSoup, browser, flagExternal)

                dataTrue["Menú"].append('transparencia')
                dataTrue["Requisitos"].append(requisite.keyword[0])
                dataTrue["Existe"].append(onPage)
                dataTrue["URL"].append(address)
                dataTrue["Titulo"].append(title)
                dataTrue["Descripción"].append(info)
                dataTrue["Última modificación"].append(date)

                break
              
        if not flagExistence:
            dataFalse["URL"].append(address)
            dataFalse["Requisito"].append(requisite.keyword[0])

    return dataTrue, dataFalse
    
    




if __name__ == "__main__":
    sys.tracebacklimit = 0
    if len(sys.argv) == 1:
        print("USO: python app.py <url>")
        print("USO: python app.py <url1> <url2> <url3> ...")
        raise ValueError("No se proporcionó ninguna URL")
    elif len(sys.argv) == 2:
        urlList = [formatUrl(sys.argv[1])]
    else:
        urlList = []
        for indx, addr in enumerate(sys.argv):
            if(indx != 0):
                urlList.append(formatUrl(addr))


    # # Initial settings
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser =  webdriver.Chrome(options=chrome_options)


    ## Compute & print all requisites in console
    dataTrueDfList = [] 
    dataFalseDfList = []
    for addr in urlList:
        dataTrueFilled, dataFalseFilled = computeRequisites(addr, dataTrueTemplate, dataFalseTemplate, requisitesList)
        dataTrueDf, dataFalseDf = printRequisites(dataTrueFilled, dataFalseFilled)
        dataTrueDfList.append(dataTrueDf)
        dataFalseDfList.append(dataFalseDf)

    ## Save in Excel
    dataframesToExcel(dataTrueDfList, "output/Requisitos.xlsx")
    dataframesToExcel(dataFalseDfList, "output/No existen.xlsx")

    # Close browser
    browser.quit()

