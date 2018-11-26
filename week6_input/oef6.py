#oef6
import requests


def download():
    params = {"format":"json", "language":"nl"}
    response = requests.get("http://data.kortrijk.be/sport/outdoorlocaties.json", params)
    if response.status_code == 200:
        response_json = response.json()
        print(response_json)
        return response_json
    else:
        return none

def outdoor():
    namen = set()
    for sportcomplex in json_data:
        namen.add(sportcomplex["benaming"])
    return namen

json_data = download()
print(outdoor())