from django.shortcuts import render

from app.models import Chirp

# Create your views here.


def index_view(request):
    print(request.POST)
    if request.POST:
        chirp_body = request.POST["chirp_body"]
        if chirp_body != "":
            Chirp.objects.create(body=chirp_body)
    context = {
        "all_chirps": Chirp.objects.all().order_by("-created")
    }
    return render(request, 'index.html', context)


def about_view(request):
    print("goodbye_world")
    message = request.GET("message", "")
    voice = request.GET("message", "")
    if message:
        print("{}{}".format(message, voice))
        print(request.GET)
    context = {
    }
    return render(request, 'about.html', context)
