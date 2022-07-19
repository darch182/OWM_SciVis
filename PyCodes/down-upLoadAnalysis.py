from asyncio.windows_events import NULL
from cProfile import label
from turtle import down
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mtp
from mplcursors import cursor as cursor
#cursor(hover=True)
import seaborn as sns
import decimal
import os
import math as math
sns.set()
Settimana = {
    0: 'Lunedì',
    1: 'Martedì',
    2: 'Mercoledì',
    3: 'Giovedì',
    4: 'Venerdì',
    5: 'Sabato',
    6: 'Domenica',
}
Municipio = {
    "OWM Zona1" : "Municipio 1",
    "OWM Zona2" : "Municipio 2",
    "OWM Zona3" : "Municipio 3",
    "OWM Zona4" : "Municipio 4",
    "OWM Zona5" : "Municipio 5",
    "OWM Zona6" : "Municipio 6",
    "OWM Zona7" : "Municipio 7",
    "OWM Zona8" : "Municipio 8",
    "OWM Zona9" : "Municipio 9",
}
municipi = ["Municipio 1", "Municipio 2", "Municipio 3", "Municipio 4", "Municipio 5", "Municipio 6", "Municipio 7", "Municipio 8", "Municipio 9",]
downloadTraffic = pd.read_csv(r'C:\Unimi\VisualizzazioneScientifica\dataset\open_wifi_project\OWM_SciVis\Datasets\sessiondownloadtraffic.csv', sep=';')
uploadTraffic = pd.read_csv(r'C:\Unimi\VisualizzazioneScientifica\dataset\open_wifi_project\OWM_SciVis\Datasets\sessionuploadtraffic.csv', sep=';')
downloadTraffic = pd.DataFrame (downloadTraffic, columns=[ 'Tipologia_API', 'Zona', 'Data', 'Valore'])
uploadTraffic = pd.DataFrame (uploadTraffic, columns=[ 'Tipologia_API', 'Zona', 'Data', 'Valore'])
downloadTraffic['Data'] = pd.to_datetime(downloadTraffic['Data'])
uploadTraffic['Data'] = pd.to_datetime(uploadTraffic['Data'])
downloadTraffic["Valore"] = downloadTraffic["Valore"].apply(np.float64)
uploadTraffic["Valore"] = uploadTraffic["Valore"].apply(np.float64)
def byteIntoGB(value):
    return (value/(math.pow(10,9)))
def dayOfTheWeek(data):
    return dt.datetime.weekday(data)
downloadTraffic['ValoreInGbytes'] = list(map(byteIntoGB, downloadTraffic['Valore']))
uploadTraffic['ValoreInGbytes'] = list(map(byteIntoGB, uploadTraffic['Valore']))
trafficTemp = downloadTraffic.copy()
trafficTemp.rename(columns={"ValoreInGbytes": "Download"}, inplace=True)
trafficTemp["Upload"] = uploadTraffic["ValoreInGbytes"]



trafficTemp['DayOfTheWeek'] = list(map(dayOfTheWeek, trafficTemp['Data']))
trafficTemp['DayOfTheWeekString'] = list(map(lambda x: Settimana[x], trafficTemp['DayOfTheWeek']))
del trafficTemp["Tipologia_API"]
del trafficTemp["Valore"]
print(trafficTemp)

trafficByDayANDZoneD = trafficTemp.copy().groupby(['Zona', 'DayOfTheWeek', 'DayOfTheWeekString'])['Download'].sum().reset_index(name = "DownloadTotal")
trafficByDayANDZoneU = trafficTemp.copy().groupby(['Zona', 'DayOfTheWeek', 'DayOfTheWeekString'])['Upload'].sum().reset_index(name = "UploadTotal")
trafficByDayANDZone = trafficByDayANDZoneD.copy()
trafficByDayANDZone["UploadTotal"] = trafficByDayANDZoneU["UploadTotal"]

#print(trafficByDayANDZone)

for i in range(1,10,1):
    zonaInteressata = "OWM Zona"+str(i)
    MunicipioInteressato = "Municipio " +str(i)
    print(zonaInteressata)
    trafficZoneVariable= trafficByDayANDZone.loc[trafficByDayANDZone['Zona'] == zonaInteressata, ['Zona', 'DayOfTheWeek', 'DayOfTheWeekString', 'DownloadTotal', 'UploadTotal']]
    trafficZoneVariable.sort_values(by='DayOfTheWeek')
    print(trafficZoneVariable)
    plotTraffic = trafficZoneVariable.plot.bar(x = "DayOfTheWeekString", y= ["DownloadTotal","UploadTotal"], xlabel = "",tick_label=1, title = MunicipioInteressato,  color = ["#00B337", "red"] )
    
    for p in plotTraffic.patches:
        plotTraffic.annotate(str(round(p.get_height(),2)), (p.get_x()+(p.get_width()*0.5), p.get_height() *1.005),  ha="center")
    plt.ylabel("GigaBytes")
    plt.xlabel("")
    plt.legend(["Traffico in Download", "Traffico in upload"])
    plt.xticks(rotation=0)
    plt.show()

trafficDownloadMean = downloadTraffic.groupby(['Zona'])['ValoreInGbytes'].mean().reset_index(name = "MeanD")
trafficUploadMean = uploadTraffic.groupby(['Zona'])['ValoreInGbytes'].mean().reset_index(name = "MeanU")
trafficMean = trafficDownloadMean
trafficMean["MeanU"] = trafficUploadMean["MeanU"]
trafficMeanForPrint = trafficMean
trafficMeanForPrint["Zona"] = municipi
print(trafficMeanForPrint)
plotMean = trafficMeanForPrint.plot.bar(x="Zona", y=["MeanD", "MeanU"], color = ["#00B337", "red"], title="Media traffico dati giornaliero per Municipio")
for p in plotMean.patches:
        plotMean.annotate(str(round(p.get_height(),2)), (p.get_x()+(p.get_width()*0.5), p.get_height() *1.005),  ha="center")
plt.ylabel("GigaBytes")
plt.xlabel("")
plt.legend(["Traffico in Download", "Traffico in upload"])
plt.xticks(rotation=0)
plt.show()

