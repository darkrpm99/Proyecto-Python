import json
import requests
from requests.api import request


respuesta = requests.get('https://api.ipify.org/?format=json')
ip = json.loads(respuesta.content)

#print("Tu ip publica es" + " " + str(ip))
