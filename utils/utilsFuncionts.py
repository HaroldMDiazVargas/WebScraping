
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
    dataframe.to_html('temp.html', index=False, justify='center') 

def printRequisites(data, noExistence):
    print("Listado de requisitos encontrados:")
    printDataframe(pd.DataFrame.from_dict(data))
    print("Listado de requisitos no encontrados:")
    printDataframe(pd.DataFrame.from_dict(noExistence))