from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView

from app.models import Chirp
from app.forms import ChirpForm


# Create your views here.

def index_view(request):
    print(request.POST)
    if request.POST:
        instance = ChirpForm(request.POST)
        if instance.is_valid():
            instance.save()
    context = {
        "form": ChirpForm(),
        "all_chirps": Chirp.objects.all().order_by("-created")
    }
    return render(request, 'index.html', context)


def about_view(request):
    print("goodbye_world")
    message = request.GET("message", "")
    if message:
        print(message, )
        print(request.POST)
    context = {
    }
    return render(request, 'about.html', context)


class ChirpView(TemplateView):
    template_name = "chirps.html"

    def get_context_data(self):
        context = {
            "all_chirps": Chirp.objects.all()
        }
        return context
