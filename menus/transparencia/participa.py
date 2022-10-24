from requisites import abstractBase
from utils.utilsFuncionts import getTextData

#1 descripción general del menú participa
class DescripcionMenu(abstractBase.Requisites):
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

#2 Diagnostico e identificación de problemas
class IdentificacionProblemas(abstractBase.Requisites):
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

#3 consulta ciudadana
class ConsultaCiudadana(abstractBase.Requisites):
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

#4 planeación y presupuesto participativo
class PlaneacionParticipativa(abstractBase.Requisites):
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

#4 Control ciudadano/social
class ControlCiudadano(abstractBase.Requisites):
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

#5 Rendición de cuentas
class RendicionCuentas(abstractBase.Requisites):
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