# pylint: disable=E1101

from requisites import abstractBase
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By


class Duties(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):

        if (soup.select_one(".content_text")):
            dutiesLink = browser.find_element(By.CSS_SELECTOR, "a[href*='funciones-y-deberes']")
            # dutiesLink = browser.find_element(By.PARTIAL_LINK_TEXT, "Funciones y deberes")  #content-ti > span
            dutiesLink.click()
            sleep(3)
        redirectSoup = BeautifulSoup(browser.page_source, "html.parser")
        dates = redirectSoup.select_one(".dateMc-wrap").select("span")
        info = redirectSoup.select_one(".content-descri p").getText()
        if info:
            info = info[:self.maxCharacters]
        # print(dates)
        if (dates[0].string[-19:] == dates[1].string[-19:]):
            onPage = False
            # return 
        else:
            onPage = True

        return onPage, info, dates[0].string[-19:]