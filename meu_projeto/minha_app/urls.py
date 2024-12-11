
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contatos/', views.contatos, name='contatos'),
    path('sobre/', views.sobre, name='sobre')
]
