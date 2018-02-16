import requests
import json

url = "https://swapi.co/api/people/1"
path = '/home/chrismvelez/Desktop/luke_skywalker.json'

source = requests.get(url)

python_format = source.json()

s = json.dumps(python_format)

with open(path, 'w') as fobject:
    fobject.write(s)

with open(path) as f:
    readFile = f.read()

print (readFile)
