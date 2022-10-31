
from tqdm import tqdm

# Menu - Normatividad
class Normativa():
    def __init__(self, requisites) -> None:
        self.requisites = requisites
    
    def computeMenu(self,  url, soup, browser, dataTrue, dataFalse, dataCrossed):
        # accordionItems = soup.select(".accordion-item-text")
        for requisite in tqdm(self.requisites):
            # flagExistence = False

            dataCrossed["Requisites"].append(requisite.keyword[0])
            dataCrossed[url].append("-")
            onPage, date, title, info, address = requisite.checkRequisites(soup, browser, False)

            dataTrue["Menú"].append(requisite.menu)
            dataTrue["Requisitos"].append(requisite.keyword[0])
            dataTrue["Existe"].append(onPage)
            dataTrue["URL"].append(address)
            dataTrue["Titulo"].append(title)
            dataTrue["Descripción"].append(info)
            dataTrue["Última modificación"].append(date)

                    
                
            # if not flagExistence:
            #     dataFalse["URL"].append(url)
            #     dataFalse["Requisitos"].append(requisite.keyword[0])
            #     dataCrossed[url].append("X")

        return dataTrue, dataFalse, dataCrossed