import json

responseData = '[{"_id": "649097d25ad4866a5366bcf3", "title": "ggml", "dateTime": "2023-06-19 18:00:50 UTC", "uuid": "2960d2bf-f3fd-4340-957f-1c4fa748485d", "counter": 0, "stats": "Null", "__v": 0}]'

# print(json.loads(responseData)[0])

var = 'ggml'

i = 0
while i != len(json.loads(responseData)):
    # io = responseData[i]["stats"]
    # print(io)

    statsArr = json.loads(responseData)[i]['stats']

    
    if statsArr != 'Null':
        x = 0
        print('For Title: ' + var + '\n')
        while len(statsArr) != x:
            print('Time Opened: ' + str(statsArr[x]['time']) + ', ' + 'IP Address: ' + str(statsArr[x]['ip']), '\nCountry: ' + str(statsArr[x]['country']) + ', ' + 'Region: ' + str(statsArr[x]['regionName']) + ', ' + 'City: ' + str(statsArr[x]['city']) + ', ' + 'ZIP Code: ' + str(statsArr[x]['zip']) + '\nLatitude: ' + str(statsArr[x]['lat']) + ', ' + 'Longitude: ' + str(statsArr[x]['lon']) + '\nInternet Service Provider(ISP): ' + str(statsArr[x]['isp']) + ', ' + 'Organisation: ' + str(statsArr[x]['org']) + '\nAS number(ASN): ' + str(statsArr[x]['as']))
            print('\n')
            x += 1
    else:
        print('Time Opened: ' + 'Null' + ', ' + 'IP Address: ' + 'Null', '\nCountry: ' + 'Null' + ', ' + 'Region: ' + 'Null' + ', ' + 'City: ' + 'Null' + ', ' + 'ZIP Code: ' + 'Null' + '\nLatitude: ' + 'Null' + ', ' + 'Longitude: ' + 'Null' + '\nInternet Service Provider(ISP): ' + 'Null' + ', ' + 'Organisation: ' + 'Null' + '\nAS number(ASN): ' + 'Null')
        
    
    i += 1 
    
    