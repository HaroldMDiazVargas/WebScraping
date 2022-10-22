# pylint: disable=E1101


from requisites import abstractBase


class Organigrama(abstractBase.Requisites):

    
    def checkRequisites(self, soup, browser):
        organigramaImg = soup.select_one("img[alt=Organigrama]")
        organigramaInfo=  soup.select_one(".content-descri p").getText()
        organigramaDate = soup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
        
        if organigramaInfo:
            organigramaInfo = organigramaInfo[:self.maxCharacters]
        if(organigramaImg):
            onPage = True
        else:
            onPage = False
        return onPage, organigramaInfo, organigramaDate