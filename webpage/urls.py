from django.contrib import admin
from django.urls import path
from webpage import views

urlpatterns = [
    path('', views.index, name="homePage"),
    path('about', views.about, name="aboutpage")
]