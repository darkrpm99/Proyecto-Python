import json
import requests
import os

from requests.api import request


urlip = "https://api.ipify.org/?format=json"

respuesta = requests.get('https://api.ipify.org/?format=json')
ip = json.loads(respuesta.content)

print("Tu ip publica es" + " " + str(ip))
