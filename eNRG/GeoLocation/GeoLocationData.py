import json
import urllib.request
from xml.etree import ElementTree as ET


def GetCountries():
    xml = urllib.request.urlopen("http://www.webservicex.net/country.asmx/GetCountries").read()
    value = ET.fromstring(xml)
    if value:
        print ('Found value:', value.text)

GetCountries()