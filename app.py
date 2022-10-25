# pylint: disable=E0110
# pylint: disable=E1121
# pylint: disable=E0611
 

from utils.utilsFuncionts import *
from bs4 import BeautifulSoup
from time import sleep
import sys
from tqdm import tqdm


def computeRequisites(url, dataTrue, dataFalse, requisites ):
    
    browser.get(url + "transparencia")
    sleep(0.3) 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    accordionItems = soup.select(".accordion-item-text")

    print("Obteniendo los requisitos...")
    for requisite in tqdm(requisites):
        # print(f"Requisito {requisite.keyword[0]}")
        flagExistence = False
       
        # for  item in enumerate(accordionItems):
        for item in  accordionItems:
            # print("hola")
            # print((idx/len(accordionItems))*100)
            # pbar.update((idx/len(accordionItems))*100)
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
            dataFalse["No existen"].append(requisite.keyword[0])

    return dataTrue, dataFalse
    
    


if __name__ == "__main__":
    sys.tracebacklimit = 0
    if len(sys.argv) == 1:
        print("USO: python app.py <url>")
        print("USO: python app.py <url1> <url2> <url3> ...")
        raise ValueError("No se proporcionó ninguna URL")
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        url = "http://"+url if not "http" in url else url
        url =  url +'/' if url[-1] != "/" else url
        print("URL =", url)
    else:
        url = []
        for indx, address in enumerate(sys.argv):
            if(indx != 0):
                url.append(address)



    
    # # Initial settings
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # browser =  webdriver.Chrome(options=chrome_options)
 

    # # Compute all requisites
    # dataTrue, dataFalse = computeRequisites(url, dataTrueTemplate, dataFalseTemplate, requisitesList)
    # browser.quit()

    # # Get data and work with it
    # # arrayData, columns = convertToArray(data, notData)
    # dataTrueDf,dataFalseDf = printRequisites(dataTrue, dataFalse)
    # dataframeToHTML(dataTrueDf)
    # dataframeToHTML(dataFalseDf)

