# from django.shortcuts import render
from django.views.generic import TemplateView

import requests

from bs4 import BeautifulSoup

# Create your views here.


class SongView(TemplateView):
    template_name = "song.html"

    def get_context_data(self, song_url):
        context = super().get_context_data()
        page = requests.get("http://metrolyrics.com/" + song_url)
        souper = BeautifulSoup(page.text, "html.parser")
        context["song_lyrics"] = souper.find(id="lyrics-body-text")
        return context


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.GET:
            base_url = "http://api.metrolyrics.com/v1//multisearch/all/X-API-KEY/196f657a46afb63ce3fd2015b9ed781280337ea7/format/json?find={}&theme=desktop"
            data = requests.get(base_url.format(self.request.GET.get("song_title"))).json()
            print("you searched te pres bsorutg0rj")
            results = data["results"]["songs"]["d"]
            urls = []
            for result in results:
                urls.append(result["u"])
            context["song_urls"] = urls
        return context
