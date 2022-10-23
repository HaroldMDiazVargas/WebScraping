
import numpy as np
import pandas as pd

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

def convertToArray(data, dataByUrl):
    arrayData = np.empty((len(dataByUrl["keywords"]), len(dataByUrl)), dtype=object)
    arrayDynamic = np.empty((len(dataByUrl["keywords"]), len(dataByUrl)), dtype=object)

    count = 0
    for urlData in data:
        columns = []
        for cols in range(len(urlData)):  #measurements
            # print(urlData[cols])
            columns.append(urlData[cols][0])
            for rows in range(len(urlData[cols][1])):
            # for rows in range(len(keywords)):    #requisites
                # print(urlData[cols][1][rows])
                # arrayData[rows][cols] = urlData[cols][1][rows]
                arrayData[rows][cols] = urlData[cols][1][rows]
        if (count != 0):
            # con = np.concatenate((arrayData,arrayDynamic),axis=1)
            arrayDynamic = np.vstack((arrayDynamic, arrayData))
        if (count == 0):
            arrayDynamic[:][:] = arrayData[:][:]
            count = count +1
    return arrayDynamic, columns
# def concatData(allData, dataWebsite):
#     allData.append(dataWebsite)

def exportXlsx(arrayData, columns, filename="data.xlsx" ):
    df = pd.DataFrame(arrayData, columns= columns)
    df.to_excel(excel_writer = filename)

    print("Proccessed succesfully")
