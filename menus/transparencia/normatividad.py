
from requisites import abstractBase
from utils.utilsFuncionts import getTextData



# 1 Normatividad de la entidad
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

#2 Vinculo al diario o gaceta oficial
class VinculoGacetaOficial(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#3 Politicas, lineamientos y manuales
class PoliticaLineamientos(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)
          



#4 Busqueda de Normas
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
        return onPage, date, title, info[:self.maxCharacters], browser.current_url


#5 Proyecto de normas para comentarios
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