#oef6



def download():
    params = {"format":"json", "language":"nl"}
    response = requests.get("http://data.kortrijk.be/sport/outdoorlocaties.json", params)
    if response.status_code == 200:
        response_json = response.json()
        print(response_json)
        return response_json
    else:
        return none

download()