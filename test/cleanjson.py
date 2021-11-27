import json

def cleanJson(originalJson):
    with open(originalJson, encoding='utf8') as jsonFile:
        jsonObject = (json.load(jsonFile))["results"]
        jsonFile.close()

    cleanedJson = []

    for i in jsonObject:
        insertDictionary = {}
        for key, value in i.items():
            if key == "geometry":
                insertDictionary["location"] = value["location"]
            elif key == "name":
                insertDictionary["name"] = value
            elif key == "vicinity":
                insertDictionary["vicinity"] = value
            
        cleanedJson.append(insertDictionary)
    jsonfile = {'data': cleanedJson}

    with open('cleaned' + originalJson + '.json', 'w') as f:
        json.dump(jsonfile, f)
    

        
    