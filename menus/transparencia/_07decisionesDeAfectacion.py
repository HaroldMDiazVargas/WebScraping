# pylint: disable=E1101
from requisites import abstractBase


class DecisionesAfectacion(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".content_text")):
            date = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            # title = soup.select_one(".content_text").select_one(".content-tit span").getText()
            title = soup.select_one(".content_text").select_one(".docu--tit").getText() #span before
            info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            date = "-"
            title = soup.select_one(".section-tit").getText()
            info = soup.select_one(".content-descri").getText()
            onPage = True

        # if (soup.select_one(".content_text")):
        #     budgetDate = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        #     budgetInfo = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
        #     onPage = True
        else:
            onPage = False
            date = "-"
            title = "-"
            info = "-"
        # print(budgetDate)
        return onPage, date, title, info, browser.current_url