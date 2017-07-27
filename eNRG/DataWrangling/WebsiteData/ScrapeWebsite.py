import json
import re
import requests
from bs4 import BeautifulSoup
from jsonfinder import jsonfinder

##url = "http://www.thinkgeoenergy.com/map/"

def GetJSONObjectFromWebpage (url, JSONObject):
    page = requests.get(url).text

    #text_to_find = 'db_marker_array'

    soup = BeautifulSoup(page)

    for script in soup.find_all('script', type="text/javascript"):
        print(script)
    
        #for node in nodevisitor.visit(tree):
        #    if isinstance(node, ast.Assign):
        #        value = getattr(node.right, 'value', '')
        #        if text_to_find in value:
        #            print(value)