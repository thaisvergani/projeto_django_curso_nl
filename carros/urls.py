from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^carros/$', views.carros),
    url(r'^fabricantes/$', views.fabricantes),
    url(r'^carros/(?P<carro_id>[0-9]+)/$', views.detail)


]
