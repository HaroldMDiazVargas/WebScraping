# pylint: disable=E0110
# pylint: disable=E1121

 
from items.organigram import Organigram
from items.duties import Duties
from items.generalBudget import GeneralBudget
from items.anualHistoric import AnualHistoric 
from items.functionariesDirectory import ServersDirectory
from items.anualBuyPlan import AnualBuyPlan
from items.contractExecution import ContractExecution
from items.normativity import Normativity
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
    ['organigrama'], 
    ['funciones y deberes'], 
    ['presupuesto general'],
    [ 'histórica anual', 'ejecución presupuestal'],
    [ 'información de servidores', 'directorio de servidores públicos'],
    ['plan anual de adquisiciones'],
    [ 'ejecución de contratos'],
    [ 'normatividad']

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
    "info":[], 
    "ultMod": []
}  


# Information to gather
# obj__organigram = Organigram(keywords[0], MAX_CHARACTERS)
# obj__duties = Duties(keywords[1], MAX_CHARACTERS)
# obj__generalBudget = GeneralBudget(keywords[2], MAX_CHARACTERS)
# obj__anualHistoric = AnualHistoric(keywords[3], MAX_CHARACTERS)
# obj__serverDirectory = ServersDirectory(keywords[4], MAX_CHARACTERS)
# obj__anualBuyPlan = AnualBuyPlan(keywords[5], MAX_CHARACTERS)
# obj__contractExec = ContractExecution(keywords[6], MAX_CHARACTERS)
# obj__normativity = Normativity(keywords[7], MAX_CHARACTERS)

obj__organigram = Organigram(keywordsList[0], MAX_CHARACTERS)
obj__duties = Duties(keywordsList[1], MAX_CHARACTERS)
obj__generalBudget = GeneralBudget(keywordsList[2], MAX_CHARACTERS)
obj__anualHistoric = AnualHistoric(keywordsList[3], MAX_CHARACTERS)
obj__serverDirectory = ServersDirectory(keywordsList[4], MAX_CHARACTERS)
obj__anualBuyPlan = AnualBuyPlan(keywordsList[5], MAX_CHARACTERS)
obj__contractExec = ContractExecution(keywordsList[6], MAX_CHARACTERS)
obj__normativity = Normativity(keywordsList[7], MAX_CHARACTERS)

objects = [obj__organigram, obj__duties, obj__generalBudget, obj__anualHistoric, obj__serverDirectory, obj__anualBuyPlan, obj__contractExec, obj__normativity   ]
browser = webdriver.Chrome()
baseRef = 1037
amountUrls = 100
urls = urls[baseRef:baseRef+amountUrls] # 100 a 200
# print(urls)
listNotExist = [1035, 1036, 1042]
# urls = ['http://www.altobaudo-choco.gov.co']
for url in urls:
    
    dataByUrl["Existe"] = []  
    dataByUrl["url"] = []
    dataByUrl["info"] = []
    dataByUrl["ultMod"] = []
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
                link = item.select_one("a")
                hrefLink = url+link.get("href")

          
                browser.get(hrefLink)
                sleep(3)
                print(count," word: ", obj.keyword)
                count = count+1
                childSoup = BeautifulSoup(browser.page_source, "html.parser")
                onPage, info, ultMod = obj.checkRequisites(childSoup, browser)

                dataByUrl["Existe"].append(onPage)
                dataByUrl["url"].append(hrefLink)
                dataByUrl["info"].append(info)
                dataByUrl["ultMod"].append(ultMod)


                break
    tupla = list(dataByUrl.items())
    data.append(tupla)

print(data)
arrayData, columns = convertToArray(data, dataByUrl, keywords)
exportXlsx(arrayData,columns ) # 3rd arg optional => Filename.xlsx
browser.quit()


# arrayData = np.empty((len(keywords), len(dataByUrl)), dtype=object)
# arrayDynamic = np.empty((len(keywords), len(dataByUrl)), dtype=object)

# count = 0
# for urlData in data:
#     columns = []
#     for cols in range(len(urlData)):
#         # print(urlData[cols])
#         columns.append(urlData[cols][0])
#         for rows in range(len(keywords)):
#             # print(urlData[cols][1][rows])
#             arrayData[rows][cols] = urlData[cols][1][rows]
#     if (count != 0):
#         # con = np.concatenate((arrayData,arrayDynamic),axis=1)
#         arrayDynamic = np.vstack((arrayDynamic, arrayData))
#     if (count == 0):
#         arrayDynamic[:][:] = arrayData[:][:]
#         count = count +1

# df = pd.DataFrame(arrayDynamic, columns= columns)
# df.to_excel(excel_writer = "data.xlsx")

# print("Proccessed succesfully")
