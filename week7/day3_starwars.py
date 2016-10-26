import requests
import time

url = "https://swapi.co/api/people/1/"

json_result = requests.get(url).json()

films = json_result.get("films", "")
print(json_result)

for film in films:
    film_result = requests.get(film).json()
    split_crawl = film_result["opening_crawl"].split("\r\n")
    for line in split_crawl:
        print(line)
        time.sleep(1)
