from requisites import abstractBase

# 01 Presupuesto General
class PresupuestoGeneral(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 02 Ejecución Presupuestal Anual
class EjecucionPresupuestal(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 03 Plan de accion
class PlanAccion(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 04 Proyectos de Inversion
class ProyectosInversion(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 05 Informes de Empalme
class InformesEmpalme(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 06 Información publica y/o relevante
class InformacionPublica(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)
# 07 Informes de gestión, evaluación y auditoría
class InformesGestion(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)


# 08 Informes de la oficina de control interno
class InformesInterno(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 09 Informes sobre defensa pública y prevención del daño antijurídico
class InformeDefensaPublica(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)

# 10 Informes trimestrales sobre acceso a información, quejas y reclamos
class InformesTrimestrales(abstractBase.Requisites):
    def checkRequisites(self, soup, browser, newUrl):
        return super().checkRequisites(soup, browser, newUrl)