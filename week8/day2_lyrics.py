import requests


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


# ############### All Songs
body = requests.get(next_page, headers=headers)
souper = BeautifulSoup(body.text, "html.parser")
all_a_tags = souper.findAll("a")[33:290]
song_link_list = []
for counter, tag in enumerate(all_a_tags):
    if not tag.get("rel") and tag.get("href"):
        song_link_list.append(tag.get("href"))

for song_link in song_link_list:
    new_song_link = song_link.replace("..", "http://www.azlyrics.com")
    song_page = requests.get(new_song_link, headers=headers)
    souper = BeautifulSoup(song_page.text, "html.parser")
    all_divs = souper.findAll("div")
    song_div = all_divs[22]
    # for counter, div in enumerate(all_divs):
    #     print(counter, div)
    print(song_div.text)
    input()

# print(song_link_list)

# for counter, tag in enumerate(all_a_tags):
#     print(tag)

# <a href="http://www.azlyrics.com/l/linkinpark.html" target="_blank"><b>LINKIN PARK </b>
