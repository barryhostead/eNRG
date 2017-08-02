import json
import urllib.request
from xml.etree import ElementTree as ET
import folium

#import numpy
#import pandas as pd

#def GetWellChoices(InputFile):
#    pd_csv = pd.read_csv(InputFile)

#    well = [pd_csv.Id, pd_csv.Country, pd_csv.State, pd_csv.City, pd_csv.well]
   
#    print(well)

#GetWellChoices('C:\\Users\\barry\\Documents\\GitHub\\eNRG\\eNRG.UI\\resources\\wells.csv')


def CreateMap(lat,lon):
    map_object = folium.Map(location=[lat, lon], zoom_start=6)

    #for well in wells:
        
        #marker = folium.features.Marker(well[0], well[1], popup="Well")
        #map_object.add_child(marker)
    
        
    folium.Map.save(map_object, "C:\\Users\\barry\\Documents\\GitHub\\eNRG\\eNRG.UI\\app\\static\\py\\map.html")

