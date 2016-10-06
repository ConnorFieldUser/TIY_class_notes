from django.shortcuts import render
# Create your views here.

import datetime

from record_store.models import Song


def index_view(request):
    context = {
        "my_name": "Connor",
        "now": datetime.datetime.now(),
        "all_songs": Song.objects.all()
    }
    return render(request, 'index.html', context)


def lyrics_view(request, song_id):
    context = {
        "song": Song.objects.get(id=song_id)
    }
    return render(request, 'lyrics.html', context)
