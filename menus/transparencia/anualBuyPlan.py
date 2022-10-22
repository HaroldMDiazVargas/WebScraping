# pylint: disable=E1101


from requisites import abstractBase


class AnualBuyPlan(abstractBase.Requisites):

    
    def checkRequisites(self, soup, browser):
       
        if (soup.select_one(".content_text")):
            budgetDate = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            budgetInfo = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
            onPage = True
        else:
            onPage = False
            budgetDate = "-"
            budgetInfo = "-"
        # print(budgetDate)
        return onPage, budgetInfo, budgetDate, browser.current_url