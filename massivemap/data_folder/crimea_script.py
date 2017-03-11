import json
import os
from massivemap.models import WeatherStation
from django.contrib.gis.geos import Point
base = os.getcwd()
crima_folder = os.path.join(base, 'massivemap', 'data_folder')
print crima_folder

def get_coordinate_dict():
    crimea_file = os.path.join(crima_folder, 'crimea.json')
    with open(crimea_file, 'r') as file:
        jsondata = json.load(file)

    coordinates=jsondata['geometry']['coordinates'][0]
    name='Crimea'
    for i in coordinates:
        print name, i
        lng = i[0]
        lat = i[1]
        WeatherStation(name=name, geom=Point(lng, lat)).save()