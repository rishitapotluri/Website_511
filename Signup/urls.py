from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from Home.views import home
#from Login.views import login

from . import views

urlpatterns = [
    url(r'^home',include('Home.urls')),
    url(r'^', views.signup,name='signup'),
]


