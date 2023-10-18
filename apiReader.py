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


createPath = ""
ageDict = dict()
prov = open("provincias.txt", "r", encoding="utf8")
series = open("seriesINE.txt", "r", encoding="utf8")

for i in range(1,52):
    provName = prov.readline()
    print(provName)
    ageVector = []

    for j in range(1, 35):
        path = series.readline(9)
        createPath = "https://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/" + path + "?date=20230101:20230106"
        api_edad = fetch_data_from_api(createPath)
        midDict = api_edad["Data"]
        ageValue = midDict[0]["Valor"]
        ageVector.append(ageValue)
        series.readline()

    ageDict[provName] = ageVector


createJson("age.json",ageDict)
prov.close()
series.close()
