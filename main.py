import requests
import json
import os
from requests.models import Response

# DO NOT PUT YOUR LOCALHOST URL HERE, INSTEAD TRY DEPLOYING IT ON HEROKU, AWS, ETC. 
# OR USE NGROK TO GET AN TEMPORARY URL
# 
# EXAMPLE WITH NGROK:- 
# url = 'https://9a90-43-242-115-265.ngrok.io/'

url = 'https://doNotPutLocalHostHere.com/'     #THIS WILL NOT WORK IF YOU ENTER YOUR LOCAL URL

def create():
    title = input('enter title: ')
    myobj = {'title': title}
    responseData = requests.post(url, data = myobj)
    os.system('cls')
    print(url + str(json.loads(responseData.content.decode("utf-8"))['uuid']))
    print('\n\n\n')
    
def getData():
    response = requests.get(url + 'data')
    responseData = json.loads(response.content.decode("utf-8"))    # responseData = json.loads(yasd)
    os.system('cls')
    # print(responseData)
    i = 0
    while i != len(responseData):
        print('Title: ' + str(responseData[i]['title']) + ', ' + 'Created: ' + str(responseData[i]['dateTime']), '\nNumber of times opened: ' + str(responseData[i]['counter']) + ', ' + 'Tracking ID: ' + str(responseData[i]['uuid']))
        print('\n')
        i += 1 

def info():
    response = requests.get(url + 'data')
    responseData = json.loads(response.content.decode("utf-8"))    # responseData = json.loads(yasd)
    
    main = input('Return Info by \n(1) Title (2) Tracking ID \n=>')
    
    if main == '1':    
        i = 0
        var = input('Enter Title\n=>')
        os.system('cls')
        print('\n\n')
        while i != len(responseData):
            if str(responseData[i]['title']) == var:
                statsArr = json.loads(responseData[i]['stats'])
                x = 0
                print('For Title: ' + var + '\n')
                while len(statsArr) != x:
                    print('Time Opened: ' + str(statsArr[x]['time']) + ', ' + 'IP Address: ' + str(statsArr[x]['ip']), '\nCountry: ' + str(statsArr[x]['country']) + ', ' + 'Region: ' + str(statsArr[x]['regionName']) + ', ' + 'City: ' + str(statsArr[x]['city']) + ', ' + 'ZIP Code: ' + str(statsArr[x]['zip']) + '\nLatitude: ' + str(statsArr[x]['lat']) + ', ' + 'Longitude: ' + str(statsArr[x]['lon']) + '\nInternet Service Provider(ISP): ' + str(statsArr[x]['isp']) + ', ' + 'Organisation: ' + str(statsArr[x]['org']) + '\nAS number(ASN): ' + str(statsArr[x]['as']))
                    print('\n')
                    x += 1
                break
            i += 1 
    
    if main == '2':    
        i = 0
        var = input('Enter Tracking ID(Example:- 5359ebc0-c4f2-49b5-9074-0ce0adb03a6e)\n=>')
        os.system('cls')
        print('\n\n')
        while i != len(responseData):
            if str(responseData[i]['uuid']) == var:
                statsArr = json.loads(responseData[i]['stats'])
                x = 0
                print('For Tracking ID: ' + var + '\n')
                while len(statsArr) != x:
                    print('Time Opened: ' + str(statsArr[x]['time']) + ', ' + 'IP Address: ' + str(statsArr[x]['ip']), '\nCountry: ' + str(statsArr[x]['country']) + ', ' + 'Region: ' + str(statsArr[x]['regionName']) + ', ' + 'City: ' + str(statsArr[x]['city']) + ', ' + 'ZIP Code: ' + str(statsArr[x]['zip']) + '\nLatitude: ' + str(statsArr[x]['lat']) + ', ' + 'Longitude: ' + str(statsArr[x]['lon']) + '\nInternet Service Provider(ISP): ' + str(statsArr[x]['isp']) + ', ' + 'Organisation: ' + str(statsArr[x]['org']) + '\nAS number(ASN): ' + str(statsArr[x]['as']))
                    print('\n')
                    x += 1
                break
            i += 1

while True:
    print("<============================>")
    main = input('1) create a tracking url \n2) get all the active urls \n3) get active url info \n=>')
    if main == '1':
        create()
    if main == '2':
        getData()
    if main == '3':
        info()
