from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',search,name="search"),
    path('counter/',counter,name='counter')
]
