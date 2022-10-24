
from requisites import abstractBase
from utils.utilsFuncionts import getTextData

# 15 Normatividad de la entidad
class NormatividadEntidad(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        onPage = False
        date = "-"
        title = "-"
        info = "-"

        if (newUrl):
            onPage = True
            info = "URL Externa"
            return onPage, date, title, info[:self.maxCharacters], browser.current_url

        
        elif(soup.select_one(".norm-row")):
            date = getTextData(soup.select_one(".norm-row").select_one("i[ng-bind$='date']"))
            title = getTextData(soup.select_one(".norm-row").select_one(".norm__name"))
            info = getTextData(soup.select_one(".norm-row").select_one(".norm__description"))
            onPage = True

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


#16 Busqueda de Normas
class BusquedaNormas(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        onPage = False
        date = "-"
        title = "-"
        info = "-"

        if (newUrl):
            onPage = True
            info = "URL Externa"
            return onPage, date, title, info[:self.maxCharacters], browser.current_url

        elif(soup.select_one(".norm-row")):
            date = getTextData(soup.select_one(".norm-row").select_one("i[ng-bind$='date']"))
            title = getTextData(soup.select_one(".norm-row").select_one(".norm__name"))
            info = getTextData(soup.select_one(".norm-row").select_one(".norm__description"))
            onPage = True

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

        # elif (soup(text=lambda t: "Registrarse" in t.text)):
        #     info = "Ubicado en sitio web externo"
        #     title = "-"
        #     onPage = True
        #     date = "-"
            
        # print(budgetDate)
        return onPage, date, title, info[:self.maxCharacters], browser.current_url


#17 Proyecto de normas para comentarios
class NormasParaComentarios(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        onPage = False
        date = "-"
        title = "-"
        info = "-"

        if (newUrl):
            onPage = True
            info = "URL Externa"
            return onPage, date, title, info[:self.maxCharacters], browser.current_url

        elif(soup.select_one(".norm-row")):
            date = getTextData(soup.select_one(".norm-row").select_one("i[ng-bind$='date']"))
            title = getTextData(soup.select_one(".norm-row").select_one(".norm__name"))
            info = getTextData(soup.select_one(".norm-row").select_one(".norm__description"))
            onPage = True

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