from django.shortcuts import render
# from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from app.models import Chirp
from app.forms import ChirpForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# TemplateView

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


class ChirpView(ListView):
    template_name = "chirps.html"
    model = Chirp


class ChirpDetailView(DetailView):
    model = Chirp


class ChirpCreateView(CreateView):
    model = Chirp
    success_url = "/chirps"
    fields = ('body',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class ChirpUpdateView(UpdateView):
    model = Chirp
    success_url = "/chirps"
    fields = ('body', )


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/chirps"
