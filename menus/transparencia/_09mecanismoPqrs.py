# pylint: disable=E1101
from requisites import abstractBase


class MecanismoPqrs(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".section-tit")):
            date = "-"
            title = soup.select_one(".section-tit").getText()
            info = soup.select_one(".wrap-pqrs").getText()[:self.maxCharacters]
            onPage = True

        # if (soup.select_one(".content_text")):
        #     budgetDate = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        #     budgetInfo = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
        #     onPage = True
        else:               # PQRS de otra pagina externa!!!
            onPage = False
            date = "-"
            title = "-"
            info = "-"
        # print(budgetDate)
        return onPage, date, title, info