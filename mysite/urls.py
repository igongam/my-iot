"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from iottest.views import keyboard
from iottest.views import answer
from iottest.views import temperature
from iottest.views import humidity 

urlpatterns = [
    url(r'^keyboard/', keyboard, name='keyboard'),
    url(r'^message',answer,name='answer'),
    url(r'^temperature/(?P<temperature>\w+)$',temperature,name='temperature'),
    url(r'^humidity/(?P<humidity>\w+)$',humidity,name='humidity'),
]
