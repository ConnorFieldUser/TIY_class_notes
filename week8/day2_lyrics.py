import requests

import time

from bs4 import BeautifulSoup

headers = {
    "user-agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"

}

# ############# Find artist
search_url = "http://search.azlyrics.com/search.php?q="
artist = "linkin+park"
body = requests.get(search_url + artist)
souper = BeautifulSoup(body.text, "html.parser")
all_a_tags = (souper.findAll("a"))
next_page = all_a_tags[28].get("href")

time.sleep(2)


# ############### All Songs
body = requests.get(next_page, headers=headers)
print(body.text)


# for counter, tag in enumerate(all_a_tags):
#     print(tag)

# <a href="http://www.azlyrics.com/l/linkinpark.html" target="_blank"><b>LINKIN PARK </b>
