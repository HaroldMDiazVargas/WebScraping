from requisites import abstractBase

#1 procesos de recaudo de rentas locales
class ProcesosRecaudo(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

#2 tarifas de liquidación del impuesto de industria y comercio
class TarifasLiquidacionICA(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)