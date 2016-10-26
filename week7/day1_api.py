import requests


url = "http://swapi.co/api/species/"


def get_data(endpoint, lookup="name"):
    url = "http://swapi.co/api/{}/".format(endpoint)
    while url:
        result = requests.get(url)
        json_result = result.json()

        for species in json_result["results"]:
            print(species[lookup])

        if input("Press enter to keep going, "):
            break

        url = json_result["next"]

while True:
    value = input("Search: ")
    get_data(value)
