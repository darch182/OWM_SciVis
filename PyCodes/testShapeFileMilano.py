from tkinter.ttk import Style
import os
from matplotlib import style
import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))
shp_path = "C:/Unimi/VisualizzazioneScientifica/dataset/open_wifi_project/OWM_SciVis/Datasets/shapefileMunicipi/Municipi.shp"
assert os.path.exists(shp_path), "Input file does not exist."
sf = shp.Reader(shp_path)
len(sf.shapes())
print (len(sf.shapes())) #number of polygon in my shapefile
sf.records()
print(sf.records())
def read_shapefile(sf):
    #fetching the heading from the shapefile
    fields = [x[0] for x in sf.fields][1:]

    #fetching the records from the shapefile
    records = [list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]

    #converting shapefile data into pandas dataframe
    df = pd.DataFrame(columns=fields, data=records)

    #assign the coordinates
    df.assign(coords=shps)
    return df

df = read_shapefile(sf)
df.shape
print (df.shape)

def plot_shape(id, s=None):
    plt.figure()
    #plotting the graphical axes where map ploting will be done
    ax = plt.axes()
    ax.set_aspect('equal')
    #storing the id number to be worked upon
    shape_ex = sf.shape(id)
    #NP.ZERO initializes an array of rows and column with 0 in place of each elements 
    #an array will be generated where number of rows will be(len(shape_ex,point))and number of columns will be 1 and stored into the variable
    x_lon = np.zeros((len(shape_ex.points),1))
    #an array will be generated where number of rows will be(len(shape_ex,point))and number of columns will be 1 and stored into the variable
    y_lat = np.zeros((len(shape_ex.points),1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
    #plotting using the derived coordinated stored in array created by numpy
    plt.plot(x_lon,y_lat) 
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=10)
    # use bbox (bounding box) to set plot limits
    plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
    plt.show()
    return x0, y0

DIST_NAME = 'Milano'
#to get the id of the city map to be plotted
#com_id = df[df.MUNICIPIO == 1].index.get_values()[0]
#plot_shape(com_id, DIST_NAME)
#sf.shape(com_id)
#print(df[df.MUNICIPIO == 1].index)
#print(df[(df.MUNICIPIO == 1)].index[0])
#plot_shape(0, "Milano")
#sf.shape(0)


def plot_map(sf, x_lim = None, y_lim = None, figsize = (11,9)):
    plt.figure(figsize = figsize)
    
    for shape in sf.shapeRecords():
        id=shape.record["MUNICIPIO"]
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')
        if (x_lim == None) & (y_lim == None):
            xMin = np.amin(x)
            xMax = np.amax(x)
            yMin = np.amin(y)
            yMax = np.amax(y)
            yMed = (yMin+yMax)/2
            xMed = (xMax+xMin)/2
            #x0 = np.mean(x)
            #y0 = np.mean(y)
            #x0= np.average(x)
            #y0 = np.average(y)
            plt.text(xMed , yMed, 'Municipio '+ str(id), fontsize=9, style="normal", color='red', weight="bold", ha='center', va='center')
        print("x[0]")
        print(x[0])
     
    if (x_lim != None) & (y_lim != None):     
        plt.xlim(x_lim)
        plt.ylim(y_lim)
    plt.show()
#calling the function and passing required parameters to plot the full map
plot_map(sf)


