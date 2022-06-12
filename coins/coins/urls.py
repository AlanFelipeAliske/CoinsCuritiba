
from django import views
from django.contrib import admin
from django.urls import path
from core import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inicio/', views.inicio),
    path('sobre/', views.sobre),
    path('servicos/', views.servicos),
    path('contato/', views.contato),
    path('login/', views.login_user),
]
