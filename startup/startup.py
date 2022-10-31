
# pylint: disable=E0611
# pylint: disable=E1121
 
from menus.atencion.atencion import ItemsAtencion
from menus.normatividad.normatividad import ListaNormas
from menus.noticias.noticias import ListaNoticias
from menus.participacion.participacion import ItemsParticipa
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
from startup.transparencia.parent import Transparencia
from startup.atencion.parent import Atencion
from startup.participa.parent import Participa
from startup.noticias.parent import Noticias
from startup.normatividad.parent import Normativa

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
    "URL": [],
    "Requisitos": []
}

requisitesTransparencia = [
# Información de la entidad
Deberes("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][0], MAX_CHARACTERS),
Organigrama("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][1], MAX_CHARACTERS),
cartasDescriptivas("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][2], MAX_CHARACTERS),
DirectorioInstitucional("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][3], MAX_CHARACTERS),
DirectorioServidores("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][4], MAX_CHARACTERS),
DirectorioEntidades("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][5], MAX_CHARACTERS),
DirectorioAgremiaciones("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][6], MAX_CHARACTERS),
ProcedimientosDecisiones("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][7], MAX_CHARACTERS),
MecanismoPqrs("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][8], MAX_CHARACTERS),
CalendarioActividades("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][9], MAX_CHARACTERS),
DecisionesAfectacion("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][10], MAX_CHARACTERS),
MecanismosVigilancia("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][11], MAX_CHARACTERS),
PublicacionCV("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][12], MAX_CHARACTERS),
ProtocolosAtencion("transparencia", keywordsDict["Transparencia"]["InfoEntidad"][13], MAX_CHARACTERS),

# Normatividad
NormatividadEntidad("transparencia", keywordsDict["Transparencia"]["Normatividad"][0], MAX_CHARACTERS),
VinculoGacetaOficial("transparencia", keywordsDict["Transparencia"]["Normatividad"][1], MAX_CHARACTERS),
PoliticaLineamientos("transparencia", keywordsDict["Transparencia"]["Normatividad"][2], MAX_CHARACTERS),
BusquedaNormas("transparencia", keywordsDict["Transparencia"]["Normatividad"][3], MAX_CHARACTERS),
NormasParaComentarios("transparencia", keywordsDict["Transparencia"]["Normatividad"][4], MAX_CHARACTERS),

# Contratacion
PlanAdquisiciones("transparencia", keywordsDict["Transparencia"]["Contratacion"][0], MAX_CHARACTERS),
InfoContractual("transparencia", keywordsDict["Transparencia"]["Contratacion"][1], MAX_CHARACTERS),
EjecucionContratos("transparencia", keywordsDict["Transparencia"]["Contratacion"][2], MAX_CHARACTERS),
ManualContratacion("transparencia", keywordsDict["Transparencia"]["Contratacion"][3], MAX_CHARACTERS),
FormatosContratos("transparencia", keywordsDict["Transparencia"]["Contratacion"][4], MAX_CHARACTERS),

# Planeacion
PresupuestoGeneral("transparencia", keywordsDict["Transparencia"]["Planeacion"][0], MAX_CHARACTERS),
EjecucionPresupuestal("transparencia", keywordsDict["Transparencia"]["Planeacion"][1], MAX_CHARACTERS),
PlanAccion("transparencia", keywordsDict["Transparencia"]["Planeacion"][2], MAX_CHARACTERS),
ProyectosInversion("transparencia", keywordsDict["Transparencia"]["Planeacion"][3], MAX_CHARACTERS),
InformesEmpalme("transparencia", keywordsDict["Transparencia"]["Planeacion"][4], MAX_CHARACTERS),
InformacionPublica("transparencia", keywordsDict["Transparencia"]["Planeacion"][5], MAX_CHARACTERS),
InformesGestion("transparencia", keywordsDict["Transparencia"]["Planeacion"][6], MAX_CHARACTERS),
InformesInterno("transparencia", keywordsDict["Transparencia"]["Planeacion"][7], MAX_CHARACTERS),
InformeDefensaPublica("transparencia", keywordsDict["Transparencia"]["Planeacion"][8], MAX_CHARACTERS),
InformesTrimestrales("transparencia", keywordsDict["Transparencia"]["Planeacion"][9], MAX_CHARACTERS),

# Trámites y servicios
TramitesServicios("transparencia", keywordsDict["Transparencia"]["Tramites"][0], MAX_CHARACTERS),

# Participa
DescripcionMenu("transparencia", keywordsDict["Transparencia"]["Participa"][0], MAX_CHARACTERS),
IdentificacionProblemas("transparencia", keywordsDict["Transparencia"]["Participa"][1], MAX_CHARACTERS),
ConsultaCiudadana("transparencia", keywordsDict["Transparencia"]["Participa"][2], MAX_CHARACTERS),
PlaneacionParticipativa("transparencia", keywordsDict["Transparencia"]["Participa"][3], MAX_CHARACTERS),
ControlCiudadano("transparencia", keywordsDict["Transparencia"]["Participa"][4], MAX_CHARACTERS),
RendicionCuentas("transparencia", keywordsDict["Transparencia"]["Participa"][5], MAX_CHARACTERS),


# DatosAbiertos
GestionInfo("transparencia", keywordsDict["Transparencia"]["DatosAbiertos"][0], MAX_CHARACTERS),
DatosAbiertos("transparencia", keywordsDict["Transparencia"]["DatosAbiertos"][1], MAX_CHARACTERS),

# GrupoInteres
InfoNiños("transparencia", keywordsDict["Transparencia"]["GrupoInteres"][0], MAX_CHARACTERS),
InfoMujeres("transparencia", keywordsDict["Transparencia"]["GrupoInteres"][1], MAX_CHARACTERS),
InfoAdicional("transparencia", keywordsDict["Transparencia"]["GrupoInteres"][2], MAX_CHARACTERS),

# InfoTributaria
ProcesosRecaudo("transparencia", keywordsDict["Transparencia"]["InfoTributaria"][0], MAX_CHARACTERS),
TarifasLiquidacionICA("transparencia", keywordsDict["Transparencia"]["InfoTributaria"][1], MAX_CHARACTERS),
]

requisitesAtencion = [
    ItemsAtencion("atención", keywordsDict["Atención"]["Atención"][0], MAX_CHARACTERS),
]


requisitesParticipa = [
    ItemsParticipa("participa", keywordsDict["Participa"]["Participa"][0], MAX_CHARACTERS),
]


requisitesNoticia = [
    ListaNoticias("noticia", keywordsDict["Noticias"]["Noticias"][0], MAX_CHARACTERS),
]

requisitesNormatividad = [
    ListaNormas("normatividad", keywordsDict["Normatividad"]["Normatividad"][0], MAX_CHARACTERS),
]
  
requisitesMenus = {
    "transparencia": Transparencia(requisitesTransparencia),
    "atención": Atencion(requisitesAtencion),
    "participa": Participa(requisitesParticipa),
   "noticias": Noticias(requisitesNoticia),
   "normatividad": Normativa(requisitesNormatividad),
}


