
import numpy as np
import pandas as pd
from tabulate import tabulate


def wordExists(word, item):
    if (len(word) > 1):
        for key in word:
            if (key in item.string.lower()):
                return True
    else:
        return word[0] in item.string.lower()

def getTextData(htmlItem):
    try:
        text = htmlItem.getText()
        return text
    except AttributeError:
        return "-"

def convertToArray(data):

    count = 0
    for urlData in data:
        columns = []
     
        arrayData = np.empty((len(urlData[0][1]), len(urlData)), dtype=object)

        for cols in range(len(urlData)):  
            columns.append(urlData[cols][0])
            for rows in range(len(urlData[cols][1])):
                arrayData[rows][cols] = urlData[cols][1][rows]

        if (count != 0):
            arrayDynamic = np.vstack((arrayDynamic, arrayData))
        if (count == 0):
            arrayDynamic = arrayData
            count = count +1
    return arrayDynamic, columns


def exportXlsx(arrayData, columns, filename="data.xlsx" ):
    df = pd.DataFrame(arrayData, columns= columns)
    df.to_excel(excel_writer = filename)

    print("Proccessed succesfully")


def dataframeFromArray(arrayData, columns):
    df = pd.DataFrame(arrayData, columns= columns)
    printDataframe(df)

def dataframeFromList(listData, columnName=["No existen"]):
    df = pd.DataFrame(listData, columns=columnName)
    printDataframe(df)

def printDataframe(dataframe):
    print(tabulate(dataframe, headers='keys', tablefmt='psql', showindex=False))


def dataframeToHTML(dataframe):
    dataframe.to_html('temp.html', index=False, justify='center') 

def printRequisites(arrayData, columns, noExistence):
    print("Listado de requisitos encontrados:")
    dataframeFromArray(arrayData, columns)
    print("Listado de requisitos no encontrados:")
    dataframeFromList(noExistence)