
from tqdm import tqdm
from time import sleep
from utils.utilsFuncionts import wordExists
from bs4 import BeautifulSoup

# Menu - Transparencia
class Transparencia():
    def __init__(self, requisites) -> None:
        self.requisites = requisites
    
    def computeMenu(self,  url, soup, browser, dataTrue, dataFalse, dataCrossed):
        accordionItems = soup.select(".accordion-item-text")
        for requisite in tqdm(self.requisites):
            flagExistence = False
            dataCrossed["Requisites"].append(requisite.keyword[0])
            for item in  accordionItems:
                if wordExists(requisite.keyword, item):
                    flagExistence = True
                    dataCrossed[url].append("-")
                    link = item.select_one("a").get("href")
                    if ("http") in link:
                        hrefLink = link
                        flagExternal = True
                    else:
                        hrefLink = url+link
                        flagExternal = False
                    browser.get(hrefLink)
                    sleep(0.5)
                    
                    childSoup = BeautifulSoup(browser.page_source, "html.parser")
                    onPage, date, title, info, address = requisite.checkRequisites(childSoup, browser, flagExternal)

                    dataTrue["Menú"].append(requisite.menu)
                    dataTrue["Requisitos"].append(requisite.keyword[0])
                    dataTrue["Existe"].append(onPage)
                    dataTrue["URL"].append(address)
                    dataTrue["Titulo"].append(title)
                    dataTrue["Descripción"].append(info)
                    dataTrue["Última modificación"].append(date)

                    break
                
            if not flagExistence:
                dataFalse["URL"].append(url)
                dataFalse["Requisitos"].append(requisite.keyword[0])
                dataCrossed[url].append("X")

        return dataTrue, dataFalse, dataCrossed