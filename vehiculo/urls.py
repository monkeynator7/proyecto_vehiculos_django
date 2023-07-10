
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('add/register', views.addvehiculo, name='addvehiculo'),
    path('registro/', views.register_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('listado/', views.listado_view, name='registro'),
]
