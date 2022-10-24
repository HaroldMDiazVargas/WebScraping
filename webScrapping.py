# pylint: disable=E0110
# pylint: disable=E1121
# pylint: disable=E0611
 

from utils.utilsFuncionts import *
from selenium import webdriver
from bs4 import BeautifulSoup
from startup.startup import  objects, dataByUrl
from time import sleep
import csv

# if len(sys.argv) == 1:
#     print("USAGE: python app.py <url>")
# else:
#     url = sys.argv[1]
#     print("URL", url)
# sys.argv


urls = []

with open("websites.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)
  for row in csvreader:
    urls.append("http://www."+row[0])

 
data = []



browser = webdriver.Chrome()
baseRef = 1037
amountUrls = 100
urls = urls[baseRef:baseRef+amountUrls] # 100 a 200
# print(urls)
listNotExist = [1035, 1036, 1042]
urls = [ 'https://www.tunja-boyaca.gov.co', 
     'http://www.altobaudo-choco.gov.co', 
    'http://www.armenia-antioquia.gov.co', 
    'http://www.aguasconfuturoesp.gov.co'
    ] 


def computeRequisites(url,URLData, requisites ):
    URLData["menu"] = []
    URLData["keywords"] = []
    URLData["Existe"] = []  
    URLData["url"] = []
    URLData["Titulo"] = []
    URLData["Info"] = []
    URLData["UltimaModif"]= []
    browser.get(url + "/transparencia")
    sleep(5) 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    accordionItems = soup.select(".accordion-item-text")
    count = 1
    for requisite in requisites:
        for item in accordionItems:
            if wordExists(requisite.keyword, item):
                link = item.select_one("a").get("href")
                if ("http") in link:
                    hrefLink = link
                    flagExternal = True
                else:
                    hrefLink = url+link
                    flagExternal = False
                browser.get(hrefLink)
                sleep(3)
                # print(count," word: ", requisite.keyword)
                count = count+1
                childSoup = BeautifulSoup(browser.page_source, "html.parser")
                onPage, date, title, info, address = requisite.checkRequisites(childSoup, browser, flagExternal)

                URLData["menu"].append('transparencia')
                URLData["keywords"].append(requisite.keyword[0])
                URLData["Existe"].append(onPage)
                URLData["url"].append(address)
                URLData["Titulo"].append(title)
                URLData["Info"].append(info)
                URLData["UltimaModif"].append(date)


                break
    
    tupla = list(URLData.items())
    data.append(tupla)
    # print(data)
    
    

# computeRequisites()
if __name__ == "__main__":
    # computeRequisites(urls[0],dataByUrl, objects)
    for singleUrl in urls:
        computeRequisites(singleUrl,dataByUrl, objects)
    arrayData, columns = convertToArray(data)
    printDataframe(arrayData, columns )
    # exportXlsx(arrayData,columns ) # 3rd arg optional => Filename.xlsx

    browser.quit()
# for url in urls:
#     dataByUrl["menu"] = []
#     dataByUrl["keywords"] = []
#     dataByUrl["Existe"] = []  
#     dataByUrl["url"] = []
#     dataByUrl["Titulo"] = []
#     dataByUrl["Info"] = []
#     dataByUrl["UltimaModif"]= []
#     print(f"URL = {url}")
#     print(f"Index url {baseRef}")
#     baseRef = baseRef + 1
#     count = 1
#     browser.get(url + "/transparencia")
#     sleep(5) 
#     soup = BeautifulSoup(browser.page_source, "html.parser")
#     accordionItems = soup.select(".accordion-item-text")

#     for obj in objects:
#         for item in accordionItems:
#             if wordExists(obj.keyword, item):
#                 link = item.select_one("a").get("href")
#                 if ("http") in link:
#                     hrefLink = link
#                     flagExternal = True
#                 else:
#                     hrefLink = url+link
#                     flagExternal = False

          
#                 browser.get(hrefLink)
#                 sleep(3)
#                 print(count," word: ", obj.keyword)
#                 count = count+1
#                 childSoup = BeautifulSoup(browser.page_source, "html.parser")
#                 onPage, date, title, info, address = obj.checkRequisites(childSoup, browser, flagExternal)

#                 dataByUrl["menu"].append('transparencia')
#                 dataByUrl["keywords"].append(obj.keyword[0])
#                 dataByUrl["Existe"].append(onPage)
#                 dataByUrl["url"].append(address)
#                 dataByUrl["Titulo"].append(title)
#                 dataByUrl["Info"].append(info)
#                 dataByUrl["UltimaModif"].append(date)


#                 break
#     # print(dataByUrl)
#     tupla = list(dataByUrl.items())
#     data.append(tupla)

# print(data)
# # arrayData, columns = convertToArray(data, dataByUrl)
# arrayData, columns = convertToArray(data)
# exportXlsx(arrayData,columns ) # 3rd arg optional => Filename.xlsx
# browser.quit()
