from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from Home.views import home
from Signup.views import signup
from Details.views import details
from . import views

urlpatterns = [
    url(r'^home',include('Home.urls')),
    url(r'^details',include('Details.urls')),
    url(r'^signup',include('Signup.urls')),
    url(r'^', views.login,name='login'),
]


