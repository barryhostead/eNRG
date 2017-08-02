import json
import urllib.request
from xml.etree import ElementTree as ET
import numpy
import pandas as pd

def GetWellChoices():
    pd_csv = pd.read_csv('C:\\Users\\barry\\Documents\\GitHub\\eNRG\\eNRG.UI\\resources\\wells.csv')

    print(pd_csv)