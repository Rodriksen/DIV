import requests
import json


def fetch_data_from_api(api_url):
    # Send a GET request to the API URL
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data if the API returns JSON
        data = response.json()
        return data
    else:
        print("Request failed with status code {response.status_code}")
        return None

def createJson(file_path, data):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f'Data has been successfully written to {file_path}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')


api_ipv = fetch_data_from_api("https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/IPV729?date=:")
createJson("ipv.json", api_ipv)

createPath = ""
for i in range(1,52):
    for j in range(1,35):
        series = "Aaaa" # Esto hay que cambiarlo para que lea las series del txt
        createPath = "https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/" + series + "?date=20230101:20230106"


api_edad = fetch_data_from_api("https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/ECP131362?date=20230101:20230106")
createJson("edad.json", api_edad)
# Para arreglar esto hay que meter muchísimas series del INE