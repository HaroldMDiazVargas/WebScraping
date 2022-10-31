
# pylint: disable=E0110
import numpy as np
import pandas as pd
from tabulate import tabulate
from selenium.webdriver.common.by import By
from time import sleep

def wordExists(word, item):
    if (len(word) > 1):
        for key in word:
            if (key in item.string.lower()):
                return True
    else:
        return word[0] in item.string.lower()

def isAd(soup):
    if(soup.select_one(".modal-wrap")):
        return True
    return False

def skipAd(browser):
    openAd = browser.find_element(By.CSS_SELECTOR, "button[ng-click='popupContent.close()']")
    openAd.click()
    sleep(3)

def isMenu(soup):
    if (soup.select_one(".menu-wrap")):
        return True
    return False

def getMenuItems(browser):
    menusText = []
    dutiesLink = browser.find_elements(By.CSS_SELECTOR, ".nav-mainLink")
    for menuEl in dutiesLink:
        # menusText.append(menuEl.text.lower())
        menusText.append(menuEl.text)
    return menusText

def getTextData(htmlItem):
    try:
        text = htmlItem.getText()
        return text
    except AttributeError:
        return "-"

def convertToArray(data):
    for urlData in data:
        columns = []
        arrayData = np.empty((len(urlData[0][1]), len(urlData)), dtype=object)
        for i, (cols, rows) in enumerate(urlData):
            columns.append(cols)
            for j, row in enumerate(rows): 
                arrayData[j][i] = row
      
    return arrayData, columns    


def exportXlsx(arrayData, columns, filename="data.xlsx" ):
    df = pd.DataFrame(arrayData, columns= columns)
    df.to_excel(excel_writer = filename)

    print("Proccessed succesfully")


# def dataframeFromArray(arrayData, columns):
#     df = pd.DataFrame(arrayData, columns= columns)
#     printDataframe(df)

# def dataframeFromList(listData, columnName=["No existen"]):
#     df = pd.DataFrame(listData, columns=columnName)
#     printDataframe(df)

def printDataframe(dataframe):
    print(tabulate(dataframe, headers='keys', tablefmt='psql', showindex=False))
   
        
def dataframeToHTML(dataframe):
    if len(dataframe.columns) > 1:
        dataframe.to_html(dataframe.columns[1]+'.html', index=False, justify='center') 
    else:
        dataframe.to_html(dataframe.columns[0]+'.html', index=False, justify='center') 
        
def dataframesToExcel(dataframeList, filename):
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    for indx, dataframe in enumerate(dataframeList):
          dataframe.to_excel(writer, sheet_name="url"+str(indx+1))
    writer.close()
    print("Archivo exportado satisfactoriamente: ", filename)

def dictToExcel(dict, filename):
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    dataframe = pd.DataFrame.from_dict(dict)
    dataframe.to_excel(writer)
    writer.close()
    print("Archivo exportado satisfactoriamente: ", filename)



def printRequisites(data, noExistence):

    print("Listado de requisitos encontrados:")
    data = pd.DataFrame.from_dict(data)
    printDataframe(data)

    print("Listado de requisitos no encontrados:")
    noExistence = pd.DataFrame.from_dict(noExistence)
    printDataframe(noExistence)
    
    return data, noExistence


def formatUrl(url):
    url = "http://"+url if not "http" in url else url
    url =  url +'/' if url[-1] != "/" else url
    return url

def initializeDict(dict):
    for key in dict.keys():
        dict[key] = []
    