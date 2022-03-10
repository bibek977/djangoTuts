from django.contrib import admin
from django.urls import path
from webpage import views

from django.views.generic import TemplateView

# urlpatterns = [
#     path('', views.index, name="homePage"),
#     path('about', views.about, name="about"),
#     path('shop1', views.shop1, name="Shop1"),
#     path('shop2', views.shop2, name="Shop2"),
#     path('shop3', views.shop3, name="Shop3"),
# ]

urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html")),
]
