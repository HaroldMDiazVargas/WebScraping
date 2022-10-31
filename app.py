# pylint: disable=E0110
# pylint: disable=E1121
# pylint: disable=E0611
# pylint: disable=E0602


from utils.utilsFuncionts import *
from bs4 import BeautifulSoup
from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from startup.startup import dataFalseTemplate, dataTrueTemplate, requisitesMenus

def computeRequisites(url, dataTrue, dataFalse, dataCrossed, requisites):
    initializeDict(dataTrue)
    initializeDict(dataFalse)
    dataCrossed["Requisites"] = []
    dataCrossed[url] = []
    menusTemplate = ["transparencia", "atención", "participa", "noticias", "normatividad"]

    browser.get(url)
    sleep(0.3)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    
    if isAd(soup):
        skipAd(browser)
        sleep(0.3) 
        soup = BeautifulSoup(browser.page_source, "html.parser")
        
    if not isMenu(soup) :
        print("No existe la barra de navegación de: ", url)
        return dataTrue, dataFalse
    
    menusText = getMenuItems(browser)
    print("Obteniendo los requisitos de: ", url)


    for pos, menu in enumerate(menusText):
        if menusTemplate[pos] in menu.lower():
            menuLink = browser.find_element(By.LINK_TEXT, menu)
            menuLink.click()
            sleep(1)
            if menusTemplate[pos] in requisites:
                print("Menú "+ menusTemplate[pos])
                soup = BeautifulSoup(browser.page_source, "html.parser")
                requisitesParent = requisites[menusTemplate[pos]]
                dataTrue, dataFalse, dataCrossed = requisitesParent.computeMenu(url, soup, browser, dataTrue, dataFalse, dataCrossed) 
                browser.get(url)
                sleep(0.5)
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
    dataAditional = {}
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser =  webdriver.Chrome(options=chrome_options)

    ## Compute & print all requisites in console
    dataTrueDfList = [] 
    dataFalseDfList = []
    for addr in urlList:
        dataTrueFilled, dataFalseFilled = computeRequisites(addr, dataTrueTemplate, dataFalseTemplate, dataAditional, requisitesMenus)
        dataTrueDf, dataFalseDf = printRequisites(dataTrueFilled, dataFalseFilled)
        dataTrueDfList.append(dataTrueDf)
        dataFalseDfList.append(dataFalseDf)

    ## Save in Excel
    dataframesToExcel(dataTrueDfList, "output/Requisitos.xlsx")
    dataframesToExcel(dataFalseDfList, "output/No existen.xlsx")
    dictToExcel(dataAditional, "output/InfoAdicional.xlsx")
    # Close browser
    browser.quit()

