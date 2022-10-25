from requisites import abstractBase

#1 descripción general del menú participa
class DescripcionMenu(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#2 Diagnostico e identificación de problemas
class IdentificacionProblemas(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#3 consulta ciudadana
class ConsultaCiudadana(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#4 planeación y presupuesto participativo
class PlaneacionParticipativa(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#4 Control ciudadano/social
class ControlCiudadano(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#5 Rendición de cuentas
class RendicionCuentas(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)