import json
import urllib.request
import csv
import folium

def GetWells():
    Wells = ()
    fieldnames = ["ID","Country","State","City","Well","Long","Lat"]
    with open('C:\\Users\\barry\\Documents\\GitHub\\eNRG\\eNRG.UI\\resources\\wells.csv', 'r') as f:
        Wells = csv.reader(f, fieldnames)
            
    return Wells

def CreateMap(lat,lon):
    map_object = folium.Map(location=[lat, lon], zoom_start=6, )
    
    folium.Marker(location = [lat, lon], icon=folium.Icon(color='blue',icon='info-sign')).add_to(map_object)
    

    Wells = ()
    
    fieldnames = ["ID","Country","State","City","Well","Long","Lat"]
    with open('C:\\Users\\barry\\Documents\\GitHub\\eNRG\\eNRG.UI\\resources\\wells.csv', 'r') as f:
        Wells = csv.reader(f, fieldnames)
    #markers = GetWells()

    ## add a marker for every record in the filtered data, use a clustered view
    #for each in Wells:
    #    folium.Marker(
    #        location = [each[1][5],each[1][5]], popup=each[1][4],icon=folium.Icon(color='red',icon='info-sign')).add_to(map_object)
        
    
    folium.Map.save(map_object, "C:\\Users\\barry\\Documents\\GitHub\\eNRG\\eNRG.UI\\app\\static\\py\\map.html")