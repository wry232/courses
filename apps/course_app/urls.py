from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^yes/(?P<id>\d+)$', views.yes),
    # url(r'^yes/$', views.yes),
    url(r'^no/(?P<id>\d+)$', views.no),
]
