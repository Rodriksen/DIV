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
        print(f"Request failed with status code {response.status_code}")
        return None


api_edad = fetch_data_from_api("https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLE/116?page=1")
api_ipv = fetch_data_from_api("https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/25171?date=20000901:20230928")


parsed_edad = json.loads(api_edad)
