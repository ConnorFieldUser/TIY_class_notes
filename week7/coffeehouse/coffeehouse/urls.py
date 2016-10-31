"""coffeehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from menu_api.views import SpecialListCreateAPIView, SpecialDetailUpdateDestroyAPIView, IngredientListAPIView, \
                           IngredientDetailUpdateDestroyAPIView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^ingredients/$', IngredientListAPIView.as_view(), name="ingredient_list_api_view"),
    url(r'^ingredients/(?P<pk>\d+)/$', IngredientDetailUpdateDestroyAPIView.as_view(), name="ingredient_detail_update_destroy_api_view"),
    url(r'^specials/$', SpecialListCreateAPIView.as_view(), name="special_list_create_api_view"),
    url(r'^specials/(?P<pk>\d+)/$', SpecialDetailUpdateDestroyAPIView.as_view(), name="special_detail_update_destroy_api_view")
]
