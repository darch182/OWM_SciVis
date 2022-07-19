from asyncio.windows_events import NULL
from cProfile import label
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mtp
from mplcursors import cursor as cursor
#cursor(hover=True)
import seaborn as sns
import decimal
import os
uniqueUser = pd.read_csv(r'C:\Unimi\VisualizzazioneScientifica\dataset\open_wifi_project\OWM_SciVis\Datasets\uniqueuserzone.csv', sep=';')
uniqueUser = pd.DataFrame (uniqueUser, columns=[ 'Tipologia_API', 'Zona', 'Data', 'Valore'])
uniqueUser['Data'] = pd.to_datetime(uniqueUser['Data'])
sns.set()
colorArray = [[1, 0 , 0, 1]]
trendUser = uniqueUser.groupby("Data")["Valore"].sum().reset_index(name = "Somma")
#print(trendUser.iloc[1])
trendUser.plot(x = "Data", y = "Somma", title = "Trend utenti unici giornalieri in tutta Milano", xlabel="", linestyle="solid", legend=False, linewidth=1.5,  color="#ff0000")
plt.xticks(rotation=0)
plt.show()




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
asseX = {
    'x': list(Settimana.values())
}
def dayOfTheWeek(data):
    return dt.datetime.weekday(data)
colorArray = [[1, 0 , 0, 1]]
cmap = mtp.ListedColormap(colorArray)

uniqueUser['DayOfTheWeek'] = list(map(dayOfTheWeek, uniqueUser['Data']))
uniqueUser['DayOfTheWeekString'] = list(map(lambda x: Settimana[x], uniqueUser['DayOfTheWeek']))
uniqueUserByDayANDZone = uniqueUser.groupby(['Zona', 'DayOfTheWeek', 'DayOfTheWeekString'])['Valore'].sum().reset_index(name = 'Total')

for i in range(1,10,1):
    
    zonaInteressata = "OWM Zona"+str(i)
    MunicipioInteressato = "Municipio " +str(i)
    print(zonaInteressata)
    uniqueUserZoneVariable= uniqueUserByDayANDZone.loc[uniqueUserByDayANDZone['Zona'] == zonaInteressata, ['Zona', 'DayOfTheWeek', 'DayOfTheWeekString', 'Total']]
    uniqueUserZoneVariable.sort_values(by='DayOfTheWeek')
    print(uniqueUserZoneVariable)
    plotZone = uniqueUserZoneVariable.plot.bar(x = "DayOfTheWeekString", y= "Total", legend = False, xlabel = "",tick_label=1, title = MunicipioInteressato, colormap = cmap)
    
    for p in plotZone.patches:
        plotZone.annotate(str(p.get_height()), (p.get_x()+(p.get_width()*0.5), p.get_height() *1.005),  ha="center")
    plt.xticks(rotation=0)
    plt.show()
    #print("i incrementata", i)

zoneMoreUtilized = uniqueUser.groupby(['Zona'])['Valore'].mean().reset_index(name = "Mean")
zoneMoreUtilized['Zona'] = list(map(lambda x: Municipio[x], zoneMoreUtilized['Zona']))
print(zoneMoreUtilized)
plotMoreUtilized = zoneMoreUtilized.plot.bar( x = "Zona", y= "Mean", legend = False, xlabel = "", title = "Media utenti giornalieri per Municipio", colormap = cmap)
for p in plotMoreUtilized.patches:
    plotMoreUtilized.annotate(str(round(p.get_height(),2)), (p.get_x()+(p.get_width()*0.5), p.get_height() *1.005),  ha="center")
plt.xticks(rotation = 360)
plt.show()

