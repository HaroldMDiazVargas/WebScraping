
# pylint: disable=E0611
# pylint: disable=E1121
 
from menus.noticias.noticias import ListaNoticias
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
from startup.noticias.parent import Noticias
from startup.transparencia.parent import Transparencia

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
Deberes("transparencia", keywordsDict["InfoEntidad"][0], MAX_CHARACTERS),
Organigrama("transparencia", keywordsDict["InfoEntidad"][1], MAX_CHARACTERS),
# cartasDescriptivas("transparencia", keywordsDict["InfoEntidad"][2], MAX_CHARACTERS),
# DirectorioInstitucional("transparencia", keywordsDict["InfoEntidad"][3], MAX_CHARACTERS),
# DirectorioServidores("transparencia", keywordsDict["InfoEntidad"][4], MAX_CHARACTERS),
# DirectorioEntidades("transparencia", keywordsDict["InfoEntidad"][5], MAX_CHARACTERS),
# DirectorioAgremiaciones("transparencia", keywordsDict["InfoEntidad"][6], MAX_CHARACTERS),
# ProcedimientosDecisiones("transparencia", keywordsDict["InfoEntidad"][7], MAX_CHARACTERS),
# MecanismoPqrs("transparencia", keywordsDict["InfoEntidad"][8], MAX_CHARACTERS),
# CalendarioActividades("transparencia", keywordsDict["InfoEntidad"][9], MAX_CHARACTERS),
# DecisionesAfectacion("transparencia", keywordsDict["InfoEntidad"][10], MAX_CHARACTERS),
# MecanismosVigilancia("transparencia", keywordsDict["InfoEntidad"][11], MAX_CHARACTERS),
# PublicacionCV("transparencia", keywordsDict["InfoEntidad"][12], MAX_CHARACTERS),
# ProtocolosAtencion("transparencia", keywordsDict["InfoEntidad"][13], MAX_CHARACTERS),

# # Normatividad
# NormatividadEntidad("transparencia", keywordsDict["Normatividad"][0], MAX_CHARACTERS),
# VinculoGacetaOficial("transparencia", keywordsDict["Normatividad"][1], MAX_CHARACTERS),
# PoliticaLineamientos("transparencia", keywordsDict["Normatividad"][2], MAX_CHARACTERS),
# BusquedaNormas("transparencia", keywordsDict["Normatividad"][3], MAX_CHARACTERS),
# NormasParaComentarios("transparencia", keywordsDict["Normatividad"][4], MAX_CHARACTERS),

# # Contratacion
# PlanAdquisiciones("transparencia", keywordsDict["Contratacion"][0], MAX_CHARACTERS),
# InfoContractual("transparencia", keywordsDict["Contratacion"][1], MAX_CHARACTERS),
# EjecucionContratos("transparencia", keywordsDict["Contratacion"][2], MAX_CHARACTERS),
# ManualContratacion("transparencia", keywordsDict["Contratacion"][3], MAX_CHARACTERS),
# FormatosContratos("transparencia", keywordsDict["Contratacion"][4], MAX_CHARACTERS),

# # Planeacion
# PresupuestoGeneral("transparencia", keywordsDict["Planeacion"][0], MAX_CHARACTERS),
# EjecucionPresupuestal("transparencia", keywordsDict["Planeacion"][1], MAX_CHARACTERS),
# PlanAccion("transparencia", keywordsDict["Planeacion"][2], MAX_CHARACTERS),
# ProyectosInversion("transparencia", keywordsDict["Planeacion"][3], MAX_CHARACTERS),
# InformesEmpalme("transparencia", keywordsDict["Planeacion"][4], MAX_CHARACTERS),
# InformacionPublica("transparencia", keywordsDict["Planeacion"][5], MAX_CHARACTERS),
# InformesGestion("transparencia", keywordsDict["Planeacion"][6], MAX_CHARACTERS),
# InformesInterno("transparencia", keywordsDict["Planeacion"][7], MAX_CHARACTERS),
# InformeDefensaPublica("transparencia", keywordsDict["Planeacion"][8], MAX_CHARACTERS),
# InformesTrimestrales("transparencia", keywordsDict["Planeacion"][9], MAX_CHARACTERS),

# # Trámites y servicios
# TramitesServicios("transparencia", keywordsDict["Tramites"][0], MAX_CHARACTERS),

# # Participa
# DescripcionMenu("transparencia", keywordsDict["Participa"][0], MAX_CHARACTERS),
# IdentificacionProblemas("transparencia", keywordsDict["Participa"][1], MAX_CHARACTERS),
# ConsultaCiudadana("transparencia", keywordsDict["Participa"][2], MAX_CHARACTERS),
# PlaneacionParticipativa("transparencia", keywordsDict["Participa"][3], MAX_CHARACTERS),
# ControlCiudadano("transparencia", keywordsDict["Participa"][4], MAX_CHARACTERS),
# RendicionCuentas("transparencia", keywordsDict["Participa"][5], MAX_CHARACTERS),


# # DatosAbiertos
# GestionInfo("transparencia", keywordsDict["DatosAbiertos"][0], MAX_CHARACTERS),
# DatosAbiertos("transparencia", keywordsDict["DatosAbiertos"][1], MAX_CHARACTERS),

# # GrupoInteres
# InfoNiños("transparencia", keywordsDict["GrupoInteres"][0], MAX_CHARACTERS),
# InfoMujeres("transparencia", keywordsDict["GrupoInteres"][1], MAX_CHARACTERS),
# InfoAdicional("transparencia", keywordsDict["GrupoInteres"][2], MAX_CHARACTERS),

# # InfoTributaria
# ProcesosRecaudo("transparencia", keywordsDict["InfoTributaria"][0], MAX_CHARACTERS),
# TarifasLiquidacionICA("transparencia", keywordsDict["InfoTributaria"][1], MAX_CHARACTERS),
]

requisitesNoticia = [
    ListaNoticias("noticia", keywordsDict["Noticias"][0], MAX_CHARACTERS),
]


requisitesMenus = {
    "transparencia": Transparencia(requisitesTransparencia),
   "noticias": Noticias(requisitesNoticia)
}


