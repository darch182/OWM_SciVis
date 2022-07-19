import numpy as np
import matplotlib as mpl
import pandas as pd
wifiRepeater = pd.read_csv(r'C:\Unimi\VisualizzazioneScientifica\dataset\open_wifi_project\repeaterLocation.csv', sep=';')
wifiRepeater = wifiRepeater[wifiRepeater['MUNICIPIO'].notna()]
#print (wifiRepeater) intero, solo senza i municipi che sono NaN
wifiRepeater = pd.DataFrame( wifiRepeater, columns=['OBJECTID', 'MUNICIPIO'])
#print (wifiRepeater) stampa delle colonne object id e municipio
print (wifiRepeater.groupby('MUNICIPIO').count())