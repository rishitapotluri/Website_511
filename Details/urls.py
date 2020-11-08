from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from Home.views import home
#from Signup.views import signup

from . import views

urlpatterns = [
    url(r'^home',include('Home.urls')),
    url(r'^', views.details,name='details'),
]


