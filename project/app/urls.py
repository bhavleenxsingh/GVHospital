from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('faculty', views.faculty, name = "faculty"),
    path('doctor-signup', views.docsign, name = "docsign"),
    path('doctor-login', views.doclog, name = "doclog"),
    path('addpatient', views.addpatient, name = "addpatient"),
    path('patient', views.patient, name = "patient"),
    path('feedb', views.feedb, name = "feedb"),
    path('viewfeedback', views.viewfeedback, name = "viewfeedback"),
    path('about', views.about, name = "about"),
    path('pdm', views.pdm, name = "pdm"),
    path('invalidf', views.invalidf, name = "invalidf"),
    path('dne', views.dne, name = "dne"),
    path('success', views.success, name = "success"),
    path('dowhat', views.dowhat, name = "dowhat"),
    path('logout', views.logout, name = "logout"),
]
