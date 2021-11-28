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
    

        
    
input = [{'address_components': [{'long_name': 'Unit 110', 'short_name': 'Unit 110', 'types': ['subpremise']}, 
{'long_name': '13450', 'short_name': '13450', 'types': ['street_number']}, {'long_name': '102 Avenue', 'short_name': '102 Ave', 'types': ['route']}, 
{'long_name': 'Whalley', 'short_name': 'Whalley', 'types': ['neighborhood', 'political']},
 {'long_name': 'Surrey', 'short_name': 'Surrey', 'types': ['locality', 'political']}, 
 {'long_name': 'Metro Vancouver', 'short_name': 'Metro Vancouver', 'types': ['administrative_area_level_2', 'political']},
  {'long_name': 'British Columbia', 'short_name': 'BC', 'types': ['administrative_area_level_1', 'political']}, 
  {'long_name': 'Canada', 'short_name': 'CA', 'types': ['country', 'political']}, 
  {'long_name': 'V3T 0A3', 'short_name': 'V3T 0A3', 'types': ['postal_code']}], 
  'formatted_address': '13450 102 Ave Unit 110, Surrey, BC V3T 0A3, Canada', 
  'geometry': {'bounds': {'northeast': {'lat': 49.1881095, 'lng': -122.8492905}, 'southwest': {'lat': 49.1879858, 'lng': -122.8494727}}, 'location': {'lat': 49.1880494, 'lng': -122.8493724}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 49.1893966302915, 'lng': -122.8480326197085}, 'southwest': {'lat': 49.1866986697085, 'lng': -122.8507305802915}}}, 'place_id': 'ChIJmd6TsNTZhVQRytO2xQyd7cI', 'types': ['subpremise']}]



def clean_geo_result(input):


    return input[0]

clean_geo_result(input)