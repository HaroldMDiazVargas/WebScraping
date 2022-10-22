# pylint: disable=E1101

from requisites import abstractBase
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By

# 01.Funciones y deberes
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

# 02. Organigrama
class Organigrama(abstractBase.Requisites):

    
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".section-tit")):
            date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
            title = soup.select_one(".section-tit").getText()
            info = soup.select_one(".content-descri p").getText()[:self.maxCharacters]
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

# 03. Mapas y cartas descriptivas de los procesos
class cartasDescriptivas(abstractBase.Requisites):

    
    def checkRequisites(self, soup, browser):


# 04. Directorio Institucional

class DirectorioInstitucional(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".content_text")):
            date = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            title = soup.select_one(".content_text").select_one(".content-tit span").getText()
            info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            date = "-"
            title = soup.select_one(".section-tit").getText()
            info = soup.select_one(".content-descri").getText()[:self.maxCharacters]
            onPage = True
        else:
            onPage = False
            date = "-"
            title = "-"
            info = "-"
        # print(budgetDate)
        return onPage, date, title, info, browser.current_url

# 05. Directorio de servidores
class DirectorioServidores(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".content_text")):
            date = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            title = soup.select_one(".content_text").select_one(".content-tit span").getText()
            info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            date = "-"
            title = soup.select_one(".section-tit").getText()
            info = soup.select_one(".content-descri").getText()[:self.maxCharacters]
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

# 06. Directorio de entidades
class DirectorioEntidades(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
 

# 07. Directorio de agremiaciones
class DirectorioAgremiaciones(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
  

# 08. Procesos y procedimientos
class ProcedimientosDecisiones(abstractBase.Requisites):
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
            info = soup.select_one(".content-descri").getText()[:self.maxCharacters]
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


# 09. Mecanismos para presentar quejas y reclamos
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
        return onPage, date, title, info, browser.current_url
   
# 10. calendario de Actividades
class CalendarioActividades(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
       

# 11. Decisiones que pueden afectar al público}
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
            info = soup.select_one(".content-descri").getText()[:self.maxCharacters]
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

# 12. Mecanismos de vigilancia
class MecanismosVigilancia(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):
        if(soup.select_one(".content_text")):
            date = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            title = soup.select_one(".content_text").select_one(".content-tit span").getText()
            # title = soup.select_one(".content_text").select_one(".docu--tit").getText() #span before
            info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            date = "-"
            title = soup.select_one(".section-tit").getText()
            info = soup.select_one(".content-descri").getText()[:self.maxCharacters]
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


# 13. Publicación hoja de vida
class PublicacionCV(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):


# 14. Servicio al público, normas, formularios y protocolos de atención'
class ProtocolosAtencion(abstractBase.Requisites):
    def checkRequisites(self, soup, browser):