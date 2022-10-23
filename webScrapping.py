# pylint: disable=E0110
# pylint: disable=E1121

 

from menus.transparencia.informacion_entidad import *
from menus.transparencia.normatividad import *
from menus.transparencia.contratacion import *
# from menus.transparencia._01funcionesydeberes import Deberes
# from menus.transparencia._02organigrama import Organigrama
# from menus.transparencia._04directorioInstitucional import DirectorioInstitucional
# from menus.transparencia._05directorioServidores import DirectorioServidores
# from menus.transparencia._14protocolosDeAtención import ProtocoloAtencion
# from menus.transparencia._08procedimientosDecisiones import ProcedimientosDecisiones
# from menus.transparencia._11decisionesDeAfectacion import DecisionesAfectacion
# from menus.transparencia._12mecanismosVigilancia import MecanismosVigilancia
# from menus.transparencia._09mecanismoPqrs import MecanismoPqrs

from utils.utilsFuncionts import *


from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import csv

# Initial Settings
MAX_CHARACTERS = 40

urls = []

with open("websites.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)
  for row in csvreader:
    urls.append("http://www."+row[0])

 
data = []
keywordsList = [
    # Seccion1. Información de la entidad
    ['funciones y deberes'],                                                                                                                                #01
    ['organigrama'],                                                                                                                                        #02 
    ['mapas y cartas descriptivas de los procesos'],                                                                                                       #03
    ['directorio institucional'],                                                                                                                           #04
    ['información de servidores públicos', 'directorio de servidores públicos'],                                                                            #05
    ['directorio de entidades'],                                                                                                                            #06
    ['directorio de asociaciones, agremiaciones', 'directorio de agremiaciones'],                                                                                                          #07
    ['procedimientos que se siguen para tomar decisiones', 'procesos y procedimientos'],                                                                    #08
    ['mecanismos para presentar quejas y reclamos', 'mecanismo de presentación directa de solicitudes'],                                                    #09
    ['calendario de actividades'],                                                                                                                          #10
    ['decisiones que pueden afectar al público', 'decisiones que puede afectar al público'],                                                                #11
    ['autoridades que lo vigilan', 'entes de control que vigilan a la entidad','entes de control'],                                                                            #12
    ['publicación de hojas de vida'],                                                                                                                       #13
    ['servicio al público, normas, formularios y protocolos de atención', 'servicio al público, normas'],                                                                                  #14

    # Normativa
    ['normativa de la entidad', 'normatividad'],                                                                                                            #15
    ['búsqueda de normas'],                                                                                                                                 #16
    ['proyectos de normas para comentarios'],                                                                                                               #17
    
    # Contratación
    ['plan anual de adquisiciones'],                                                                                                                        #18
    ['información contractual'],                                                                                                                            #19
    ['ejecución de contratos'],                                                                                                                             #20
    ['manual de contratación, adquisición y/o compras', 
    'políticas en materia de adquisición y compras'],                                                                                                    #21
    ['formatos o modelos de contratos'],                                                                                                                    #22

    # Planeación
    ['presupuesto general'],                                                                                                                                #23
    ['ejecución presupuestal', 'histórica anual', ],                                                                                                        #24
    ['plan de acción'],                                                                                                                                     #25
    ['proyectos de inversión'],                                                                                                                             #26
    ['informes de empalme'],                                                                                                                                #27
    ['informes de gestión, evaluación y auditoría'],                                                                                                        #28
    ['informes de la oficina de control interno'],                                                                                                          #29
    ['informe sobre defensa pública y prevención del daño antijurídico'],                                                                                   #30
    ['informes trimestrales sobre acceso a información, quejas y reclamos'],                                                                                #31
    
    # Trámites
    ['trámites y servicios','trámites'],                                                                                                                    #32
    
    # # Participa
    # ['descripción general del menú participa', 'descripción general']
    # ['diagnóstico e identificación de problemas'],

    # Datos abiertos
    ['instrumentos de gestión de la información'],                                                                                                          #33
    ['sección de datos abiertos'],                                                                                                                          #34

    # Información especifica para Grupos de inter'es
    ['información para niños, niñas y adolescentes'],                                                                                                       #35
    ['información para mujeres'],                                                                                                                           #36
    
    # Información tributaria en ent terr locales
    ['procesos de recaudo de rentas locales'],                                                                                                              #37
    ['tarifas de liquidación del impuesto de industria y comercio']                                                                                         #38
 

]
keywords = [
    'organigrama', 
    'funciones y deberes', 
    'presupuesto general',
    'histórica anual',
    'información de servidores',
    'plan anual de adquisiciones',
    'ejecución de contratos',
    'normatividad'

    ]
dataByUrl = {
    'keywords':keywords, #'información de servidores'
    "Existe": [],
    "url": [],
    "Titulo":[],
    "Info":[], 
    "UltimaModif": []
}  


# Información de la entidad
# obj__deberes = Deberes(keywordsList[0], MAX_CHARACTERS)
# obj__organigrama = Organigrama(keywordsList[1], MAX_CHARACTERS)
# obj__cartas_descriptivas = cartasDescriptivas(keywordsList[2], MAX_CHARACTERS)
# obj__directorio_institucional = DirectorioInstitucional(keywordsList[3], MAX_CHARACTERS)
# obj__directorio_servidores = DirectorioServidores(keywordsList[4], MAX_CHARACTERS)
# obj__directorio_entidades = DirectorioEntidades(keywordsList[5], MAX_CHARACTERS)
# obj__directorio_agremiacion = DirectorioAgremiaciones(keywordsList[6], MAX_CHARACTERS)
# obj__procedimientos_decisiones = ProcedimientosDecisiones(keywordsList[7], MAX_CHARACTERS)
# obj__mecanismo_pqrs = MecanismoPqrs(keywordsList[8], MAX_CHARACTERS)
# obj__calendario_actividades = CalendarioActividades(keywordsList[9], MAX_CHARACTERS)
# obj__decisiones_afecta = DecisionesAfectacion(keywordsList[10], MAX_CHARACTERS)
# obj__mecanismo_vigilancia = MecanismosVigilancia(keywordsList[11], MAX_CHARACTERS)
# obj__publicacion_cv = PublicacionCV(keywordsList[12], MAX_CHARACTERS)
# obj__protocolo_atencion = ProtocolosAtencion(keywordsList[13], MAX_CHARACTERS)

# Normatividad
# obj__normatividad_entidad= NormatividadEntidad(keywordsList[14], MAX_CHARACTERS)
# obj__busqueda_normas= BusquedaNormas(keywordsList[15], MAX_CHARACTERS)
# obj__normas_comentarios = NormasParaComentarios(keywordsList[16], MAX_CHARACTERS)

# Contratacion
obj__plan_anual = PlanAdquisiciones(keywordsList[17], MAX_CHARACTERS)
obj__info_contractual= InfoContractual(keywordsList[18], MAX_CHARACTERS)
obj__ejec_contratos = EjecucionContratos(keywordsList[19], MAX_CHARACTERS)
obj__manual_contratacion = ManualContratacion(keywordsList[20], MAX_CHARACTERS)
obj__formatos_contratos = FormatosContratos(keywordsList[21], MAX_CHARACTERS)



# objects = [
# Deberes(keywordsList[0], MAX_CHARACTERS),
# Organigrama(keywordsList[1], MAX_CHARACTERS),
# cartasDescriptivas(keywordsList[2], MAX_CHARACTERS),
# DirectorioInstitucional(keywordsList[3], MAX_CHARACTERS),
# DirectorioServidores(keywordsList[4], MAX_CHARACTERS),
# DirectorioEntidades(keywordsList[5], MAX_CHARACTERS),
# DirectorioAgremiaciones(keywordsList[6], MAX_CHARACTERS),
# ProcedimientosDecisiones(keywordsList[7], MAX_CHARACTERS),
# MecanismoPqrs(keywordsList[8], MAX_CHARACTERS),
# CalendarioActividades(keywordsList[9], MAX_CHARACTERS),
# DecisionesAfectacion(keywordsList[10], MAX_CHARACTERS),
# MecanismosVigilancia(keywordsList[11], MAX_CHARACTERS),
# PublicacionCV(keywordsList[12], MAX_CHARACTERS),
# ProtocolosAtencion(keywordsList[13], MAX_CHARACTERS)
# ]


# obj__generalBudget = GeneralBudget(keywordsList[2], MAX_CHARACTERS)
# obj__anualHistoric = AnualHistoric(keywordsList[3], MAX_CHARACTERS)|
# obj__anualBuyPlan = AnualBuyPlan(keywordsList[5], MAX_CHARACTERS)
# obj__contractExec = ContractExecution(keywordsList[6], MAX_CHARACTERS)
# obj__normativity = Normativity(keywordsList[7], MAX_CHARACTERS)

objects = [
        # obj__deberes, obj__organigrama, obj__cartas_descriptivas, obj__directorio_institucional, obj__directorio_servidores, obj__directorio_entidades, obj__directorio_agremiacion, obj__procedimientos_decisiones,
        # obj__mecanismo_pqrs,obj__calendario_actividades, obj__decisiones_afecta, obj__mecanismo_vigilancia,obj__publicacion_cv, obj__protocolo_atencion,
        # obj__normatividad_entidad, obj__busqueda_normas, obj__normas_comentarios  
        obj__plan_anual, obj__info_contractual, obj__ejec_contratos, obj__manual_contratacion, obj__formatos_contratos

        ]
# objects = [obj__organigram, obj__duties, obj__generalBudget, obj__anualHistoric, obj__serverDirectory, obj__anualBuyPlan, obj__contractExec, obj__normativity   ]
browser = webdriver.Chrome()
baseRef = 1037
amountUrls = 100
urls = urls[baseRef:baseRef+amountUrls] # 100 a 200
# print(urls)
listNotExist = [1035, 1036, 1042]
urls = [ 'https://www.tunja-boyaca.gov.co', 'http://www.altobaudo-choco.gov.co', 'http://www.armenia-antioquia.gov.co', 'http://www.aguasconfuturoesp.gov.co'] # 'https://www.tunja-boyaca.gov.co', 'http://www.altobaudo-choco.gov.co',
for url in urls:
    dataByUrl["keywords"] = []
    dataByUrl["Existe"] = []  
    dataByUrl["url"] = []
    dataByUrl["Titulo"] = []
    dataByUrl["Info"] = []
    dataByUrl["UltimaModif"]= []
    print(f"URL = {url}")
    print(f"Index url {baseRef}")
    baseRef = baseRef + 1
    count = 1
    browser.get(url + "/transparencia")
    sleep(5) 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    accordionItems = soup.select(".accordion-item-text")

    for obj in objects:
        for item in accordionItems:
            if wordExists(obj.keyword, item):
                link = item.select_one("a").get("href")
                if ("http") in link:
                    hrefLink = link
                else:
                    hrefLink = url+link

          
                browser.get(hrefLink)
                sleep(3)
                print(count," word: ", obj.keyword)
                count = count+1
                childSoup = BeautifulSoup(browser.page_source, "html.parser")
                onPage, date, title, info, address = obj.checkRequisites(childSoup, browser)

                dataByUrl["keywords"].append(obj.keyword[0])
                dataByUrl["Existe"].append(onPage)
                dataByUrl["url"].append(address)
                dataByUrl["Titulo"].append(title)
                dataByUrl["Info"].append(info)
                dataByUrl["UltimaModif"].append(date)


                break
    # print(dataByUrl)
    tupla = list(dataByUrl.items())
    data.append(tupla)

print(data)
# arrayData, columns = convertToArray(data, dataByUrl)
arrayData, columns = convertToArray(data)
exportXlsx(arrayData,columns ) # 3rd arg optional => Filename.xlsx
browser.quit()
