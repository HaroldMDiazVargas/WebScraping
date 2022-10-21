from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
import json



  
# text = 'organigrama'
#  funciones-y-deberes
# presupuesto general  search on index; click and see date!!
# historico anual; search on index and click an see date!!
# directorio-de-funcionarios; directorio de información de servidores públicos
# keywords = [
#     "organigrama",
#     "funciones y deberes",
#     "presupuesto general",
#     "histórica anual",
#     "información de servidores"
# ]

urls = [
    "https://www.tunja-boyaca.gov.co/",
    "http://www.avp-planadas-tolima.gov.co/",
    "https://www.caqueta.gov.co/",
    "http://www.hospitalelbordo.gov.co/"
]

data = {
    "urls": []
}

dataByUrl = {
    'keywords':['organigrama', 'funciones y deberes', 'presupuesto general','histórica anual'], #'información de servidores'
    "Existe": [],
    "url": [],
    "info":[],
    "ultMod": []
}

# for url in urls:
#     dataByUrl["Existe"] = []  
#     dataByUrl["url"] = []
#     dataByUrl["info"] = []
#     dataByUrl["ultMod"] = []
#     for keyword in dataByUrl["keywords"]:
#         dataByUrl["Existe"].append(True)
#         dataByUrl["url"].append("ww...")
#         dataByUrl["info"].append("sasasa")
#         dataByUrl["ultMod"].append("11010")
#     data["urls"].append( {url: dataByUrl})

# print(data)
#     print("keyword")
#     data["Existe"] = 10
#     # data["url"].append(keyword+"...url")
# # data["url"] = url
# print(data)


def wordExists(word, item):
    return word in item.string.lower()

def checkOrganigram(argSoup):
    # linkargSoup = BeautifulargSoup(browser.page_source, "html.parser")
    organigramaImg = argSoup.select_one("img[alt=Organigrama]")
    organigramaInfo=  argSoup.select_one(".content-descri p").getText()
    if organigramaInfo:
        organigramaInfo = organigramaInfo[:20]
    organigramaDate = argSoup.select_one(".dateMc-wrap").select("span")[0].string[-19:]
    if(organigramaImg):
        onPage = True
    else:
        onPage = False
    return onPage, organigramaInfo, organigramaDate
    
    
    
        # print(f"Its organigram exists")

def checkDuties(argSoup):
    if (argSoup.select_one(".content_text")):
        dutiesLink = browser.find_element(By.LINK_TEXT, "Funciones y deberes")
        dutiesLink.click()
        sleep(3)
    redirectSoup = BeautifulSoup(browser.page_source, "html.parser")
    dates = redirectSoup.select_one(".dateMc-wrap").select("span")
    info = redirectSoup.select_one(".content-descri p").getText()
    if info:
        info = info[:20]
    # print(dates)
    if (dates[0].string[-19:] == dates[1].string[-19:]):
        onPage = False
        # return 
    else:
        onPage = True

    return onPage, info, dates[0].string[-19:]

    # dates.sele
    # articlesByContent= soup.select(".content_text")
    # if len(articlesByContent) > 0:
    #     for article in articlesByContent:
    #         if 

def checkBudget(argSoup):
    if (argSoup.select_one(".content_text")):
        budgetDate = argSoup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        budgetInfo = argSoup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
        onPage = True
    else:
        onPage = False
        budgetDate = ""
        budgetInfo = ""
    # print(budgetDate)
    return onPage, budgetInfo, budgetDate

def checkAnualHistoric(argsSoup):
    if (argsSoup.select_one(".content_text")):
        budgetDate = argsSoup.select_one(".content_text").select_one("p[ng-bind$='date']").getText()
        budgetInfo = argsSoup.select_one(".content_text").select_one("p[ng-bind-html$='metaDescription']").getText()
        onPage = True
    else:
        onPage = False
        budgetDate = ""
        budgetInfo = ""
    # print(budgetDate)
    return onPage, budgetInfo, budgetDate
    # return onPage, budgetInfo, budgetDate    
    

def checkPublicDirectory(soup):
    sectionContent =  soup.select(".content_text")
    for i in range(3):
        print("Date modify: ", sectionContent[i].select_one("p[ng-bind$='date']").getText())
        print("Name/Context: ", sectionContent[i].select_one(".content-tit span").getText())
        print("Content: ", sectionContent[i].select_one("p[ng-bind-html$='metaDescription']").getText())


# url = "https://www.tunja-boyaca.gov.co"
# transparenciaUrl = url + "/transparencia"

# browser = webdriver.Chrome()
# browser.get(transparenciaUrl)
# sleep(5) 




# soup = BeautifulSoup(browser.page_source, "html.parser")

# accordionItems = soup.select(".accordion-item-text")
# print(accordionItems[0].string)


browser = webdriver.Chrome()

for url in urls:
    dataByUrl["Existe"] = []  
    dataByUrl["url"] = []
    dataByUrl["info"] = []
    dataByUrl["ultMod"] = []


    browser.get(url + "/transparencia")
    sleep(5) 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    accordionItems = soup.select(".accordion-item-text")

    for word in dataByUrl["keywords"]:
        for item in accordionItems:
            if wordExists(word, item):
                # print(f"Link {word} exists")
                link = item.select_one("a")
                # print(link)
                # print(link.get("href"))
                hrefLink = url+link.get("href")
                browser.get(hrefLink)
                sleep(3)
                childSoup = BeautifulSoup(browser.page_source, "html.parser")
                if word == "organigrama":
                    # setGroup(link.get("href"))
                    onPage, info, ultMod = checkOrganigram(childSoup)
                    dataByUrl["Existe"].append(onPage)
                    dataByUrl["url"].append(hrefLink)
                    dataByUrl["info"].append(info)
                    dataByUrl["ultMod"].append(ultMod)
                
                if word == "funciones y deberes":
                    onPage, info, ultMod = checkDuties(childSoup)
                    dataByUrl["Existe"].append(onPage)
                    dataByUrl["url"].append(hrefLink)
                    dataByUrl["info"].append(info)
                    dataByUrl["ultMod"].append(ultMod)
                if word == "presupuesto general":
                    onPage, info, ultMod =checkBudget(childSoup)
                    dataByUrl["Existe"].append(onPage)
                    dataByUrl["url"].append(hrefLink)
                    dataByUrl["info"].append(info)
                    dataByUrl["ultMod"].append(ultMod)
                if word == "histórica anual":
                    onPage, info, ultMod = checkAnualHistoric(childSoup)
                    dataByUrl["Existe"].append(onPage)
                    dataByUrl["url"].append(hrefLink)
                    dataByUrl["info"].append(info)
                    dataByUrl["ultMod"].append(ultMod)
                # if word == "información de servidores":
                #     checkPublicDirectory(childSoup)
                #     dataByUrl["Existe"].append(True)
                #     dataByUrl["url"].append("ww...")
                #     dataByUrl["info"].append(hrefLink")
                #     dataByUrl["ultMod"].append("11010")

                break
    print(dataByUrl)
    data["urls"].append({url: dataByUrl})
    # print(data)

with open("sample.json", "w") as outfile:
    json.dump(data, outfile)
# json_object = json.dumps(data, indent = 4) 
# print(data)


# for word in keywords:
#     for item in accordionItems:
#         if wordExists(word, item):
#             print(f"Link {word} exists")
#             link = item.select_one("a")
#             # print(link)
#             # print(link.get("href"))
#             browser.get(url+link.get("href"))
#             sleep(3)
#             childSoup = BeautifulSoup(browser.page_source, "html.parser")
#             if word == "organigrama":
#                 # setGroup(link.get("href"))
#                 checkOrganigram(childSoup)
#             if word == "funciones y deberes":
#                 checkDuties()
#             if word == "presupuesto general":
#                 checkBudget(childSoup)
#             if word == "histórica anual":
#                 checkAnualHistoric(childSoup)
#             if word == "información de servidores":
#                 checkPublicDirectory(childSoup)

#             break

# time.sleep(3) 
# linkSoup = BeautifulSoup(browser.page_source, "html.parser")
# organigramaImg =  linkSoup.select_one("img[alt=Organigrama]")
# print(organigramaImg)



        # print(link)
        # i.click()
    # if(i.string.lower() == text):
    #     print(i)


# browser.quit()

# # Search by text with the help of lambda function
# gfg = soup.find_all(lambda tag: tag.name == "strong" and text in tag.text)
# print(soup)
# print(accordionItems[0])
# print(accordionItems[0].select("header"))
# # if (accordionItems[0].get("ng-if")):
    





# python -m venv envName
# envName/bin/activate.bat


# pip install pipenv
# pipenv install packageName
# pipenv --venv (path of venv; open and go bin/interpreter!!)
#  - settings.json
#  - "code-runner.executorMap": { "python": "path of pythogn interpreter!!" }
#  - also set interpreer of VScode!!  or => "python.pythonPath": "PathOfýutjpmInterpreter!!"
#pipenv install (pipfile and install dependencies!!) or pipenv install --ignore-pipfile! (pipfile.lock)

# pipenv shell  => activate venv (exit)
