# pylint: disable=E1101

from requisites import abstractBase
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from utils.utilsFuncionts import getTextData

# 01.Funciones y deberes
class Deberes(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):  
        onPage = False
        date = "-"
        title = "-"
        info = "-"

        if (newUrl):
            onPage = True
            info = "URL Externa"
            return onPage, date, title, info[:self.maxCharacters], browser.current_url

        elif(soup.select_one(".content_text")):
            # link = soup.select_one("a[href*='funciones-y-deberes']").get("href")

            dutiesLink = browser.find_element(By.CSS_SELECTOR, "a[href*='funciones-y-deberes']")
            dutiesLink.click()
            sleep(1)
            
            # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='documentType-0']"))).click()
        redirectSoup = BeautifulSoup(browser.page_source, "html.parser")

        if(redirectSoup.select_one(".section-tit")): 
            title = getTextData(redirectSoup.select_one(".section-tit")) 
            if (redirectSoup.select_one(".dateMc-wrap")):
                date = redirectSoup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
            
            if(redirectSoup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(redirectSoup.select_one("p[ng-bind$='file.name']"))
            
            elif(redirectSoup.select_one(".content-descri")):
                info =  getTextData(redirectSoup.select_one(".content-descri"))
                onPage = True

            if (redirectSoup(text=lambda t: "Escribe aquí las funciones y deberes" in t.text)):
                onPage = False

        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 02. Organigrama
class Organigrama(abstractBase.Requisites):

    
    def checkRequisites(self, soup, browser, newUrl):
        onPage = False
        date = "-"
        title = "-"
        info = "-"

        if (newUrl):
            onPage = True
            info = "URL Externa"
            return onPage, date, title, info[:self.maxCharacters], browser.current_url

        elif(soup.select_one(".section-tit")):
  
            date = soup.select_one(".dateMc-wrap")
            if(date):
                date = date.select("span")[0].string[-19:]
            
            title = getTextData(soup.select_one(".section-tit"))
            info = getTextData(soup.select_one(".content-descri p"))
            if (soup.select_one("img[src*='organigrama']")):          #Imagen
                onPage = True
            elif(soup.select_one("p[ng-bind$='file.name']")):       #archivo
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))
        
            else:
                onPage = False

        return onPage, date, title, info[:self.maxCharacters], browser.current_url


# 03. Mapas y cartas descriptivas de los procesos
class cartasDescriptivas(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)


# 04. Directorio Institucional

class DirectorioInstitucional(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 05. Directorio de servidores
class DirectorioServidores(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 06. Directorio de entidades
class DirectorioEntidades(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 07. Directorio de agremiaciones
class DirectorioAgremiaciones(abstractBase.Requisites):
    
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)
  

# 08. Procesos y procedimientos
class ProcedimientosDecisiones(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)


# 09. Mecanismos para presentar quejas y reclamos
class MecanismoPqrs(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        onPage = False
        date = "-"
        title = "-"
        info = "-"

        if (newUrl):
            onPage = True
            info = "URL Externa"
            return onPage, date, title, info[:self.maxCharacters], browser.current_url

        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
           
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
            
            if (soup.select_one(".wrap-pqrs")):
                info = getTextData(soup.select_one(".wrap-pqrs").getText())
                onPage = True
            else:
                onPage = False
        return onPage, date, title, info[:self.maxCharacters], browser.current_url
   
# 10. calendario de Actividades
class CalendarioActividades(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 11. Decisiones que pueden afectar al público}
class DecisionesAfectacion(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 12. Mecanismos de vigilancia
class MecanismosVigilancia(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)
        
# 13. Publicación hoja de vida
class PublicacionCV(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 14. Servicio al público, normas, formularios y protocolos de atención'
class ProtocolosAtencion(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)