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
sns.set()
colorArray = [[1, 0 , 0, 1]]
registeredUsers = pd.read_csv(r'C:\Unimi\VisualizzazioneScientifica\dataset\open_wifi_project\registered.csv', sep=';')
registeredUsers = pd.DataFrame (registeredUsers, columns=[ 'Data', 'Valore'])
registeredUsers['Data'] = pd.to_datetime(registeredUsers['Data'])
registeredUsers = registeredUsers.sort_values(by="Data")
print(registeredUsers)
registeredUsers.plot(x = "Data", y = "Valore", title = "Trend registrazioni in tutta Milano", linestyle="solid", legend=False, linewidth=1.5,  color="#ff0000")
plt.xticks(rotation=0)
plt.show()

