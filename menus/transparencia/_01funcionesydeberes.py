# pylint: disable=E1101

from requisites import abstractBase
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By


class Deberes(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".content_text")):
            dutiesLink = browser.find_element(By.CSS_SELECTOR, "a[href*='funciones-y-deberes']")
            dutiesLink.click()
            sleep(3)
        redirectSoup = BeautifulSoup(browser.page_source, "html.parser")

        if(redirectSoup.select_one(".section-tit")):
            date = redirectSoup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
            title = redirectSoup.select_one(".section-tit").getText()
            info = redirectSoup.select_one(".content-descri p").getText()[:self.maxCharacters]
            onPage = True
        else:
            onPage = False
            date = "-"
            title = "-"
            info = "-"
        return onPage, date, title, info, browser.current_url


        # dates = redirectSoup.select_one(".dateMc-wrap").select("span")
        # info = redirectSoup.select_one(".content-descri p").getText()

        #     date = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        #     # title = soup.select_one(".content_text").select_one(".content-tit span").getText()
        #     title = soup.select_one(".content_text").select_one(".docu--tit").getText() #span before
        #     info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
        #     onPage = True
        
        # elif(soup.select_one(".section-tit")):
        #     date = "-"
        #     title = soup.select_one(".section-tit").getText()
        #     info = soup.select_one(".content-descri").getText()
        #     onPage = True

        # # if (soup.select_one(".content_text")):
        # #     budgetDate = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        # #     budgetInfo = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
        # #     onPage = True
        # else:
        #     onPage = False
        #     date = "-"
        #     title = "-"
        #     info = "-"
        # # print(budgetDate)
        # return onPage, date, title, info




        # if (soup.select_one(".content_text")):
        #     dutiesLink = browser.find_element(By.CSS_SELECTOR, "a[href*='funciones-y-deberes']")
        #     # dutiesLink = browser.find_element(By.PARTIAL_LINK_TEXT, "Funciones y deberes")  #content-ti > span
        #     dutiesLink.click()
        #     sleep(3)
        # redirectSoup = BeautifulSoup(browser.page_source, "html.parser")
        # dates = redirectSoup.select_one(".dateMc-wrap").select("span")
        # info = redirectSoup.select_one(".content-descri p").getText()
        # if info:
        #     info = info[:self.maxCharacters]
        # # print(dates)
        # if (dates[0].string[-19:] == dates[1].string[-19:]):
        #     onPage = False
        #     # return 
        # else:
        #     onPage = True

        # return onPage, info, dates[0].string[-19:]