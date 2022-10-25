from requisites import abstractBase

#1 instrumentos de gestión de la información
class GestionInfo(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#2 sección de datos abiertos
class DatosAbiertos(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)