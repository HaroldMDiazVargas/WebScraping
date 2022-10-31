from requisites import abstractBase
from selenium.webdriver.common.by import By
# Menu - Noticias
class ItemsParticipa(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        onPage = False
        date = "-"
        title = "-"
        info = "-"

        if (newUrl):
            onPage = True
            info = "URL Externa"
            return onPage, date, title, info[:self.maxCharacters], browser.current_url

        items = browser.find_element(By.CSS_SELECTOR, ".nav-wLinkFirts.open").find_elements(By.CSS_SELECTOR, ".nav-BtnChild")
        allItems = ""
        for itemsText in items:
            allItems = itemsText.text + allItems + " "
        
        info = allItems
        onPage = True
        
   
        return onPage, date, title, info[:self.maxCharacters], browser.current_url