
# pylint: disable=E0611
 
from menus.transparencia.informacion_entidad import *
from menus.transparencia.normatividad import *
from menus.transparencia.contratacion import *
from menus.transparencia.planeacion import *
from menus.transparencia.tramites import *
from menus.transparencia.participa import *
from menus.transparencia.datos_abiertos import *
from menus.transparencia.grupo_interes import *
from menus.transparencia.info_tributaria import *
from requisites.keywords import keywordsDict

# Initial Settings
MAX_CHARACTERS = 40

dataTrueTemplate = {
    'Menú': [],
    'Requisitos': [], 
    "Existe": [],
    "URL": [],
    "Titulo":[],
    "Descripción":[], 
    "Última modificación": []
}  

dataFalseTemplate = {
    "No existen": []
}

requisitesList = [
# Información de la entidad
Deberes(keywordsDict["InfoEntidad"][0], MAX_CHARACTERS),
Organigrama(keywordsDict["InfoEntidad"][1], MAX_CHARACTERS),
cartasDescriptivas(keywordsDict["InfoEntidad"][2], MAX_CHARACTERS),
DirectorioInstitucional(keywordsDict["InfoEntidad"][3], MAX_CHARACTERS),
DirectorioServidores(keywordsDict["InfoEntidad"][4], MAX_CHARACTERS),
DirectorioEntidades(keywordsDict["InfoEntidad"][5], MAX_CHARACTERS),
DirectorioAgremiaciones(keywordsDict["InfoEntidad"][6], MAX_CHARACTERS),
ProcedimientosDecisiones(keywordsDict["InfoEntidad"][7], MAX_CHARACTERS),
MecanismoPqrs(keywordsDict["InfoEntidad"][8], MAX_CHARACTERS),
CalendarioActividades(keywordsDict["InfoEntidad"][9], MAX_CHARACTERS),
DecisionesAfectacion(keywordsDict["InfoEntidad"][10], MAX_CHARACTERS),
MecanismosVigilancia(keywordsDict["InfoEntidad"][11], MAX_CHARACTERS),
PublicacionCV(keywordsDict["InfoEntidad"][12], MAX_CHARACTERS),
ProtocolosAtencion(keywordsDict["InfoEntidad"][13], MAX_CHARACTERS),

# Normatividad
NormatividadEntidad(keywordsDict["Normatividad"][0], MAX_CHARACTERS),
VinculoGacetaOficial(keywordsDict["Normatividad"][1], MAX_CHARACTERS),
PoliticaLineamientos(keywordsDict["Normatividad"][2], MAX_CHARACTERS),
BusquedaNormas(keywordsDict["Normatividad"][3], MAX_CHARACTERS),
NormasParaComentarios(keywordsDict["Normatividad"][4], MAX_CHARACTERS),

# Contratacion
PlanAdquisiciones(keywordsDict["Contratacion"][0], MAX_CHARACTERS),
InfoContractual(keywordsDict["Contratacion"][1], MAX_CHARACTERS),
EjecucionContratos(keywordsDict["Contratacion"][2], MAX_CHARACTERS),
ManualContratacion(keywordsDict["Contratacion"][3], MAX_CHARACTERS),
FormatosContratos(keywordsDict["Contratacion"][4], MAX_CHARACTERS),

# Planeacion
PresupuestoGeneral(keywordsDict["Planeacion"][0], MAX_CHARACTERS),
EjecucionPresupuestal(keywordsDict["Planeacion"][1], MAX_CHARACTERS),
PlanAccion(keywordsDict["Planeacion"][2], MAX_CHARACTERS),
ProyectosInversion(keywordsDict["Planeacion"][3], MAX_CHARACTERS),
InformesEmpalme(keywordsDict["Planeacion"][4], MAX_CHARACTERS),
InformacionPublica(keywordsDict["Planeacion"][5], MAX_CHARACTERS),
InformesGestion(keywordsDict["Planeacion"][6], MAX_CHARACTERS),
InformesInterno(keywordsDict["Planeacion"][7], MAX_CHARACTERS),
InformeDefensaPublica(keywordsDict["Planeacion"][8], MAX_CHARACTERS),
InformesTrimestrales(keywordsDict["Planeacion"][9], MAX_CHARACTERS),

# Trámites y servicios
TramitesServicios(keywordsDict["Tramites"][0], MAX_CHARACTERS),

# Participa
DescripcionMenu(keywordsDict["Participa"][0], MAX_CHARACTERS),
IdentificacionProblemas(keywordsDict["Participa"][1], MAX_CHARACTERS),
ConsultaCiudadana(keywordsDict["Participa"][2], MAX_CHARACTERS),
PlaneacionParticipativa(keywordsDict["Participa"][3], MAX_CHARACTERS),
ControlCiudadano(keywordsDict["Participa"][4], MAX_CHARACTERS),
RendicionCuentas(keywordsDict["Participa"][5], MAX_CHARACTERS),


# DatosAbiertos
GestionInfo(keywordsDict["DatosAbiertos"][0], MAX_CHARACTERS),
DatosAbiertos(keywordsDict["DatosAbiertos"][1], MAX_CHARACTERS),

# GrupoInteres
InfoNiños(keywordsDict["GrupoInteres"][0], MAX_CHARACTERS),
InfoMujeres(keywordsDict["GrupoInteres"][1], MAX_CHARACTERS),
InfoAdicional(keywordsDict["GrupoInteres"][2], MAX_CHARACTERS),

# InfoTributaria
ProcesosRecaudo(keywordsDict["InfoTributaria"][0], MAX_CHARACTERS),
TarifasLiquidacionICA(keywordsDict["InfoTributaria"][1], MAX_CHARACTERS),
]