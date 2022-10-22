# pylint: disable=E1101


from requisites import abstractBase


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
        return onPage, date, title, info


        # organigramaImg = soup.select_one("img[alt=Organigrama]")
        # organigramaInfo=  soup.select_one(".content-descri p").getText()
        # organigramaDate = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
        
        # if organigramaInfo:
        #     organigramaInfo = organigramaInfo[:self.maxCharacters]
        # if(organigramaImg):
        #     onPage = True
        # else:
        #     onPage = False
        # return onPage, organigramaInfo, organigramaDate