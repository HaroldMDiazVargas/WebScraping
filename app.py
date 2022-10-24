# pylint: disable=E0110
# pylint: disable=E1121
# pylint: disable=E0611
 

from utils.utilsFuncionts import *
from selenium import webdriver
from bs4 import BeautifulSoup
from startup.startup import  objects, dataByUrl
from time import sleep
import sys



def computeRequisites(url,URLData, requisites ):

    browser.get(url + "transparencia")
    sleep(5) 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    accordionItems = soup.select(".accordion-item-text")

    
    for requisite in requisites:
        flagExistence = False
        for item in accordionItems:
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
                sleep(3)

                childSoup = BeautifulSoup(browser.page_source, "html.parser")
                onPage, date, title, info, address = requisite.checkRequisites(childSoup, browser, flagExternal)

                URLData["Menú"].append('transparencia')
                URLData["Requisito"].append(requisite.keyword[0])
                URLData["Existe"].append(onPage)
                URLData["URL"].append(address)
                URLData["Titulo"].append(title)
                URLData["Información"].append(info)
                URLData["Última modificación"].append(date)


                break
        if not flagExistence:
            noExistence.append(requisite.keyword[0])

    tupla = list(URLData.items())
    data.append(tupla)
    # print(data)
    
    


if __name__ == "__main__":
    sys.tracebacklimit = 0
    if len(sys.argv) == 1:
        print("USO: python app.py <url>")
        raise ValueError("No se proporcionó ninguna URL")
    else:
        url = sys.argv[1]
        url = "http://"+url if not "http" in url else url
        url =  url +'/' if not  url[-1] == "/" else url
        print("URL =", url)
    
    # Initial settings
    data = []
    noExistence = []
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser =  webdriver.Chrome(options=options)

    # Compute all requisites
    computeRequisites(url, dataByUrl, objects)

    # Get data and work with it
    arrayData, columns = convertToArray(data)
    printRequisites(arrayData, columns, noExistence)


    browser.quit()
