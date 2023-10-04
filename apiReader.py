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


file_path = "ipv.json"



api_ipv = fetch_data_from_api("https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/25171?date=20000901:20230928")

# Write the data to the JSON file
try:
    with open(file_path, 'w') as json_file:
        json.dump(api_ipv, json_file, indent=4)
    print(f'Data has been successfully written to {file_path}')
except Exception as e:
    print(f'An error occurred: {str(e)}')

api_edad = fetch_data_from_api("https://servicios.ine.es/wstempus/js/ES/VALORES_VARIABLE/116?page=1")

parsed_edad = json.loads(api_edad)
