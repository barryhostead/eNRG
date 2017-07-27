import json

def GetListOfElementsFromJSONFile(JSONFile, element):
     with open(JSONFile,'r') as JSONDataFile:
        JSONData = json.load(JSONDataFile)
      
        rows = len(JSONData)
        DataElementList = []
        while rows >= 0:
            row = rows-1
            DataElement = JSONData[row][element]
            DataElementID = JSONData[row]["ID"]
            #print (type(DataElement))
            if type(DataElement) is list:
                if element == "HashTags":
                    for item in DataElement:
                        DataElementList.append([DataElementID,item["text"]])
                if element == "Mentions":
                    for item in DataElement:
                        DataElementList.append([DataElementID,item["screen_name"]])
            else:
                DataElementList.append(DataElement)
            
            rows = rows-1
         
        return DataElementList