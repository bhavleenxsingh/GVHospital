from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('faculty', views.faculty, name = "faculty"),
    path('doctor-signup', views.docsign, name = "docsign"),
    path('doctor-login', views.doclog, name = "doclog"),
    path('nurse-signup', views.nursesign, name = "nursesign"),
    path('nurse-login', views.nurse, name = "nurse"),
    path('feedback', views.feedback, name = "feedback"),
    path('about', views.about, name = "about"),
    path('pdm', views.pdm, name = "pdm"),
    path('invalid', views.invalidf, name = "invalidf"),
]
