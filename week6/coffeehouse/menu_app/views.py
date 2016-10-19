# from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from menu_app.models import Special

from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.


class IndexView(ListView):
    template_name = "index.html"
    model = Special


class ProfileView(TemplateView):
    template_name = 'profile.html'


class SpecialUpdateView(UpdateView):
    model = Special
    success_url = "/"
    fields = ('title', 'description', 'cost')

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Special.objects.all()
        return Special.objects.filter(created_by=self.request.user)


class SpecialDeleteView(DeleteView):
    model = Special
    success_url = "/"

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Special.objects.all()
        return []

    #
    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context["object_list"] = Special.objects.all()
    #     return context
