# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from menu.models import Special

# Create your views here.


class SpecialListView(ListView):
    model = Special


class SpecialCreateView(CreateView):
    model = Special
    fields = ('title', 'description', 'picture')
    success_url = reverse_lazy("special_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        return super().form_valid(form)


class SpecialUpdateView(UpdateView):
    model = Special
    fields = ('title', 'description', 'picture')
    success_url = "/"
