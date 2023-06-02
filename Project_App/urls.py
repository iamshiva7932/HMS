from django.contrib import admin
from django.urls import path
from Project_App import views

urlpatterns = [
    path("" ,views.home, name='home'),
    path("index", views.index, name='index'),
    path("signin",views.signin,name='signin'),
    path('book_now',views.book_now,name='book_now'),
    path('contact',views.contact,name='contact'),
    path('new_delhi',views.new_delhi,name='new_delhi'),
    path('about_us',views.about_us,name='about_us')
]