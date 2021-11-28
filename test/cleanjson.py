import json

def cleanJson(originalJson):
    with open(originalJson, encoding='utf8') as jsonFile:
        jsonObject = (json.load(jsonFile))["results"]
        jsonFile.close()

    cleanedJson = []

    for i in jsonObject:
        if "restaurant" in i["types"]:
            for key, value in i.items():

                if key == "geometry":
                    lat = value["location"]["lat"]
                    lng = value["location"]["lng"]
        
                    cleanedJson.append([lat, lng])
    print(cleanedJson)
    

cleanJson('testJson.json')
        
