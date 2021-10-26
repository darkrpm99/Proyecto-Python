import json
import requests
from requests.api import request

respuesta = requests.get('https://api.ipify.org/?format=json')
ip = json.loads(respuesta.content)

with open('datos.json', 'w') as outfile:
    json.dump(ip, outfile)
print("datos guardados correctamente en fichero datos.json")

with open("datos.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()


text = jsonObject['ip']
print("Tu ip publica es: " + text)
