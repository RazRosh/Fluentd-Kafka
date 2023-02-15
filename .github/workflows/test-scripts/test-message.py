import requests
import time
import sys

message = sys.argv[1]
kafdrop_ip = sys.argv[2]

time.sleep(6)

param =  {
    "name": "format",
    "in": "query",
    "description": "format",
    "required": False,
    "type": "string"
}

r = requests.get('http://' + kafdrop_ip + ':9000/topic/messages/messages?partition=0&offset=0&count=100&keyFormat=DEFAULT&format=DEFAULT', params=param)
counter = 0
for i in r.text.split('{'):
    if(i.find(message) > 0):
        counter+=1

if counter == 1:
    print(1)
else:
    print(0)
