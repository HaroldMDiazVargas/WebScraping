# pylint: disable=E1101
from requisites import abstractBase


class ServersDirectory(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".content_text")):
            checkDate = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            checkInfo = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
            checkTitle = soup.select_one(".content_text").select_one(".content-tit span").getText()
            checkInfo = checkTitle+" "+checkInfo
            onPage = True

        # if (soup.select_one(".content_text")):
        #     budgetDate = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        #     budgetInfo = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
        #     onPage = True
        else:
            onPage = False
            checkDate = "-"
            checkInfo = "-"
        # print(budgetDate)
        return onPage, checkInfo, checkDate
