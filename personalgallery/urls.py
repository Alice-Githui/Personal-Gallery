from django.urls import path
from . import views

#app urls 
urlpatterns=[
    path('', views.index, name="indexpage"),
]