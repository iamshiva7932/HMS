from django.contrib import admin
from django.urls import path
from Project_App import views

urlpatterns = [
    path("" ,views.home, name='home'),
    path("index", views.index, name='index'),
    path("signin",views.signin,name='signin'),
    path('contact',views.contact,name='contact')
]