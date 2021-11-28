import requests
import json
import os
from requests.models import Response

url = 'http://localhost:3000/'

def create():
    title = input('enter title: ')
    myobj = {'title': title}
    responseData = requests.post(url, data = myobj)
    os.system('cls')
    print(json.loads(responseData.content.decode("utf-8"))['uuid'])
    print('\n\n\n')
    
def getData():
    response = requests.get(url + 'data')
    responseData = json.loads(response.content.decode("utf-8"))    # responseData = json.loads(yasd)
    os.system('cls')
    # print(responseData)
    i = 0
    while i != len(responseData):
        print('Title: ' + str(responseData[i]['title']) + ', ' + 'DateTime: ' + str(responseData[i]['dateTime']), '\nNumber of times opened: ' + str(responseData[i]['counter']) + ', ' + 'Tracking ID: ' + str(responseData[i]['uuid']))
        print('\n')
        i += 1 

while True:
    print("<============================>")
    main = input('1) create a tracking url \n2) get all the active urls \n=>')
    if main == '1':
        create()
    if main == '2':
        getData()