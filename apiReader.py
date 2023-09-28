import requests
import json

edad = requests.get("https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLE/116?page=1")
ipv = requests.get("https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/25171?date=20000901:20230928")

print(edad.status_code)

print(ipv.status_code)