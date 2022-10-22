# pylint: disable=E0110
# pylint: disable=E1121

 
 
from menus.transparencia._01funcionesydeberes import Deberes
from menus.transparencia._02organigrama import Organigrama
from menus.transparencia._03directorioInstitucional import DirectorioInstitucional
from menus.transparencia._04directorioServidores import DirectorioServidores
from menus.transparencia._05protocolosDeAtención import ProtocoloAtencion
from menus.transparencia._06procedimientosDecisiones import ProcedimientosDecisiones
from menus.transparencia._07decisionesDeAfectacion import DecisionesAfectacion
from menus.transparencia._08mecanismosVigilancia import MecanismosVigilancia
from menus.transparencia._09mecanismoPqrs import MecanismoPqrs
# from menus.transparencia.generalBudget import GeneralBudget 
# from menus.transparencia.anualHistoric import AnualHistoric 
# from menus.transparencia.anualBuyPlan import AnualBuyPlan
# from menus.transparencia.contractExecution import ContractExecution
# from menus.transparencia.normativity import Normativity
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
    ['funciones y deberes'], 
    ['organigrama'], 
    ['mapas y cartas descriptivas de los procesos' ],
    ['directorio institucional'],
    ['información de servidores públicos', 'directorio de servidores públicos'],
    ['directorio de entidades'],
    ['directorio de asociaciones, agremiaciones'],
    ['procedimientos que se siguen para tomar decisiones', 'procesos y procedimientos'],
    ['mecanismos para presentar quejas y reclamos', 'mecanismo de presentación directa de solicitudes'],
    ['calendario de actividades'],
    ['decisiones que pueden afectar al público', 'decisiones que puede afectar al público'],
    ['autoridades que lo vigilan', 'entes de control que vigilan a la entidad'],
    ['publicación de hojas de vida'],
    ['servicio al público, normas, formularios y protocolos de atención'],

    # Normativa
    ['normativa de la entidad', 'normatividad'],
    ['búsqueda de normas'],
    ['proyectos de normas para comentarios'],
    
    # Contratación
    ['plan anual de adquisiciones'],
    ['información contractual'],
    [ 'ejecución de contratos'],
    ['manual de contratación, adquisición y/o compras'],
    ['formatos o modelos de contratos'],

    # Planeación
    ['presupuesto general'],
    ['ejecución presupuestal', 'histórica anual', ],
    ['plan de acción'],
    ['proyectos de inversión'],
    ['informes de empalme'],
    ['informes de gestión, evaluación y auditoría'],
    ['informes de la oficina de control interno'],
    ['informe sobre defensa pública y prevención del daño antijurídico'],
    ['informes trimestrales sobre acceso a información, quejas y reclamos'],
    
    # Trámites
    ['trámites y servicios','trámites'],
    
    # # Participa
    # ['descripción general del menú participa', 'descripción general']
    # ['diagnóstico e identificación de problemas'],

    # Datos abiertos
    ['instrumentos de gestión de la información'],
    ['sección de datos abiertos'],

    # Información especifica para Grupos de inter'es
    ['información para niños, niñas y adolescentes'],
    ['información para mujeres'],
    
    # Información tributaria en ent terr locales
    ['procesos de recaudo de rentas locales'],
    ['tarifas de liquidación del impuesto de industria y comercio']
 

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


# Information to gather
# obj__organigram = Organigram(keywords[0], MAX_CHARACTERS)
# obj__Deberes = Deberes(keywords[1], MAX_CHARACTERS)
# obj__generalBudget = GeneralBudget(keywords[2], MAX_CHARACTERS)
# obj__anualHistoric = AnualHistoric(keywords[3], MAX_CHARACTERS)
# obj__serverDirectory = ServersDirectory(keywords[4], MAX_CHARACTERS)
# obj__anualBuyPlan = AnualBuyPlan(keywords[5], MAX_CHARACTERS)
# obj__contractExec = ContractExecution(keywords[6], MAX_CHARACTERS)
# obj__normativity = Normativity(keywords[7], MAX_CHARACTERS)

obj__deberes = Deberes(keywordsList[0], MAX_CHARACTERS)
obj__organigrama = Organigrama(keywordsList[1], MAX_CHARACTERS)
obj__directorioInst = DirectorioInstitucional(keywordsList[2], MAX_CHARACTERS)
obj__directorioServ = DirectorioServidores(keywordsList[3], MAX_CHARACTERS)
obj__protocoloAtenc = ProtocoloAtencion(keywordsList[4], MAX_CHARACTERS)
obj__procedimientoDec = ProcedimientosDecisiones(keywordsList[5], MAX_CHARACTERS)
obj__decAfectacion = DecisionesAfectacion(keywordsList[6], MAX_CHARACTERS)
obj__mecanismoVig = MecanismosVigilancia(keywordsList[7], MAX_CHARACTERS)
obj__mecanismoPqrs = MecanismoPqrs(keywordsList[8], MAX_CHARACTERS)

# obj__generalBudget = GeneralBudget(keywordsList[2], MAX_CHARACTERS)
# obj__anualHistoric = AnualHistoric(keywordsList[3], MAX_CHARACTERS)
# obj__anualBuyPlan = AnualBuyPlan(keywordsList[5], MAX_CHARACTERS)
# obj__contractExec = ContractExecution(keywordsList[6], MAX_CHARACTERS)
# obj__normativity = Normativity(keywordsList[7], MAX_CHARACTERS)

objects = [obj__deberes, obj__organigrama, obj__directorioInst, obj__directorioServ, obj__protocoloAtenc, obj__procedimientoDec, obj__decAfectacion, obj__mecanismoVig, obj__mecanismoPqrs]
# objects = [obj__organigram, obj__duties, obj__generalBudget, obj__anualHistoric, obj__serverDirectory, obj__anualBuyPlan, obj__contractExec, obj__normativity   ]
browser = webdriver.Chrome()
baseRef = 1037
amountUrls = 100
urls = urls[baseRef:baseRef+amountUrls] # 100 a 200
# print(urls)
listNotExist = [1035, 1036, 1042]
urls = ['http://www.zapatoca-santander.gov.co'] # https://www.tunja-boyaca.gov.co/transparencia
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
    print(dataByUrl)
    tupla = list(dataByUrl.items())
    data.append(tupla)

# print(data)
arrayData, columns = convertToArray(data, dataByUrl)
exportXlsx(arrayData,columns ) # 3rd arg optional => Filename.xlsx
browser.quit()
