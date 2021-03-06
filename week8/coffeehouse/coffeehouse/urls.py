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

from menu.views import SpecialListView, SpecialCreateView, SpecialUpdateView, SpecialListAPIView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SpecialListView.as_view(), name="special_list_view"),
    url(r'api/specials/$', SpecialListAPIView.as_view(), name="special_list_api_view"),
    url(r'^create/$', SpecialCreateView.as_view(), name="special_create_view"),
    url(r'^update/(?P<pk>\d+)/$', SpecialUpdateView.as_view(), name="special_update_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
