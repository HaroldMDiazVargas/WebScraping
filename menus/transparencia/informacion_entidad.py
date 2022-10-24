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
            dutiesLink = browser.find_element(By.CSS_SELECTOR, "a[href*='funciones-y-deberes']")
            dutiesLink.click()
            sleep(3)
        redirectSoup = BeautifulSoup(browser.page_source, "html.parser")

        if(redirectSoup.select_one(".section-tit")):
            date = redirectSoup.select_one(".dateMc-wrap")
            if(date):
                date = date.select("span")[0].string[-19:]

            title = getTextData(redirectSoup.select_one(".section-tit"))
            info = getTextData(redirectSoup.select_one(".content-descri p"))
            onPage = True
            # date = redirectSoup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            # title = redirectSoup.select_one(".section-tit").getText()
            # info = redirectSoup.select_one(".content-descri p").getText()
            # onPage = True
        # else:
        #     onPage = False
        #     date = "-"
        #     title = "-"
        #     info = "-"
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
            # date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
            date = soup.select_one(".dateMc-wrap")
            if(date):
                date = date.select("span")[0].string[-19:]
            
            title = getTextData(soup.select_one(".section-tit"))
            info = getTextData(soup.select_one(".content-descri p"))
            # title = soup.select_one(".section-tit").getText()
            # info = soup.select_one(".content-descri p").getText()
            if (soup.select_one("a[src*='organigrama']")):          #Imagen
                onPage = True
            elif(soup.select_one("p[ng-bind$='file.name']")):       #archivo
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))
                # info = soup.select_one("p[ng-bind$='file.name']").getText()
            else:
                onPage = False

        # if (soup.select_one(".content_text")):
        #     budgetDate = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        #     budgetInfo = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()[:self.maxCharacters]
        #     onPage = True
        
        # else:
        #     onPage = False
        #     date = "-"
        #     title = "-"
        #     info = "-"
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 03. Mapas y cartas descriptivas de los procesos
class cartasDescriptivas(abstractBase.Requisites):
    
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            if (title == '-'):
                title =  getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # date = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            # title = soup.select_one(".content_text").select_one(".content-tit span").getText()
            # title = soup.select_one(".content_text").select_one(".docu--tit").getText() #span before
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True

        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))


        # elif(soup.select_one("p[ng-bind$='file.name']")):          #Existe algun archivo adjunto
        #     title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))
                # info = soup.select_one("p[ng-bind$='file.name']").getText()

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri")) 
                # info = soup.select_one(".content-descri").getText()
                onPage = True
            else:
                onPage = False
                info="-"
        # else:
        #     onPage = False
        #     date = "-"
        #     title = "-"
        #     info = "-"
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 04. Directorio Institucional

class DirectorioInstitucional(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))
                # info = soup.select_one("p[ng-bind$='file.name']").getText()

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                # info =  soup.select_one(".content-descri").getText()
                onPage = True
            else:
                onPage = False
                info="-"
        # else:
        #     onPage = False
        #     date = "-"
        #     title = "-"
        #     info = "-"
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 05. Directorio de servidores
class DirectorioServidores(abstractBase.Requisites):
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
            # date = soup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
            # title = soup.select_one(".content_text").select_one(".content-tit span").getText()
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            # onPage = True
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True

        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
        # else:
        #     onPage = False
        #     date = "-"
        #     title = "-"
        #     info = "-"
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 06. Directorio de entidades
class DirectorioEntidades(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True

        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
           
        
        
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 07. Directorio de agremiaciones
class DirectorioAgremiaciones(abstractBase.Requisites):
    
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
        
        return onPage, date, title, info[:self.maxCharacters], browser.current_url
  

# 08. Procesos y procedimientos
class ProcedimientosDecisiones(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
        
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url


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
                info = '-'

        # elif (soup(text=lambda t: "Registrarse" in t.text)):
        #     info = "Ubicado en sitio web externo"
        #     title = "-"
        #     onPage = True
        #     date = "-"
        # elif (soup.select_one("label[for]")):
        #     info = "Ubicado en sitio web externo"
        #     title = "-"
        #     onPage = True
        #     date = '-'
                 # PQRS de otra pagina externa!!!
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url
   
# 10. calendario de Actividades
class CalendarioActividades(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True

        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 11. Decisiones que pueden afectar al público}
class DecisionesAfectacion(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
     
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 12. Mecanismos de vigilancia
class MecanismosVigilancia(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
        
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url


# 13. Publicación hoja de vida
class PublicacionCV(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"
        # elif (soup.select_one("input[type*='text']")):
        #     info = "Ubicado en sitio web externo"
        #     title = "-"
        #     onPage = True
        #     date = "-"
      
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url

# 14. Servicio al público, normas, formularios y protocolos de atención'
class ProtocolosAtencion(abstractBase.Requisites):
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
            date = getTextData(soup.select_one(".content_text").select_one("p[ng-bind$='date']"))
            title = getTextData(soup.select_one(".content_text").select_one(".content-tit span"))
            if (title == '-'):
                title = getTextData(soup.select_one(".content_text").select_one(".docu--tit"))
            info = getTextData(soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']"))
            # info = soup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
            onPage = True
        
        elif(soup.select_one(".section-tit")):
            title = getTextData(soup.select_one(".section-tit"))
            # title = soup.select_one(".section-tit").getText()
            if (soup.select_one(".dateMc-wrap")):
                date = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]

            if(soup.select_one("p[ng-bind$='file.name']")):  
                onPage = True
                info = getTextData(soup.select_one("p[ng-bind$='file.name']"))

            elif(soup.select_one(".content-descri")):
                info =  getTextData(soup.select_one(".content-descri"))
                onPage = True
            else:
                onPage = False
                info="-"

      
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url