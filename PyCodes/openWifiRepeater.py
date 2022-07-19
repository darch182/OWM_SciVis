from matplotlib.pyplot import legend, xlabel
import numpy as np
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
wifiRepeater = pd.read_csv(r'C:\Unimi\VisualizzazioneScientifica\dataset\open_wifi_project\\OWM_SciVis\Datasets\repeaterLocation.csv', sep=';')
wifiRepeater = wifiRepeater[wifiRepeater['MUNICIPIO'].notna()]
wifiRepeater["MUNICIPIO"] = wifiRepeater["MUNICIPIO"].apply(np.int64)
print (wifiRepeater) #intero, solo senza i municipi che sono NaN
wifiRepeater = pd.DataFrame( wifiRepeater, columns=['OBJECTID', 'MUNICIPIO'])
print (wifiRepeater) #stampa delle colonne object id e municipio
wifiRepeater = wifiRepeater.groupby("MUNICIPIO")["OBJECTID"].count().reset_index(name="NumberRepeater")
print(wifiRepeater)
plotRepeater = wifiRepeater.plot(kind="bar", x="MUNICIPIO", y= "NumberRepeater", title="Numero di ripetitori per Municipio", color="red", legend=False, xlabel="Municipio n°")
for p in plotRepeater.patches:
    plotRepeater.annotate(str(p.get_height()), (p.get_x()+(p.get_width()*0.5), p.get_height() *1.005),  ha="center")
plt.xticks(rotation=0)
plt.show()
