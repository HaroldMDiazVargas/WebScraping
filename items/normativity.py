# pylint: disable=E1101
from requisites import abstractBase


class Normativity(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if (soup.select_one(".norm-wTxt")):
            budgetInfo = soup.select_one(".norm-wTxt").select_one(".norm__name").getText()[:self.maxCharacters]
            budgetDate = soup.select_one(".norm-wTxt").select_one("i[ng-bind$='date']").getText()
            onPage = True
        else:
            onPage = False
            budgetDate = "-"
            budgetInfo = "-"
        # print(budgetDate)
        return onPage, budgetInfo, budgetDate