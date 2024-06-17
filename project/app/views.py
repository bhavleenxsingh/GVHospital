from django.shortcuts import render, redirect

# Create your views here.
from .forms import docregf, docloginf, nursereg, nurseregf, feedbackf, patientf
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "app/home.html")

def faculty(request):
    return render(request, "app/faculty.html")

def feedback(request):
    return render(request, "app/feedback.html")

def about(request):
    return render(request, "app/about.html")

def doclog(request):
    if request.method == "POST":
        doclogins = docloginf(request.POST)
        if doclogins.is_valid():
            Username = doclogins.cleaned_data.get('Username')
            Password = doclogins.cleaned_data.get('Password')
            user = authenticate(request, Username = Username, Password = Password)
            if user is not None:
                auth_login(request, user)
                return redirect(home)
            else:
                return HttpResponse("User does not exist")
        else:
            return redirect('invalidf')
    else:
        doclogins = docloginf()
        return render(request, "app/doctor.html", {"doclogins": doclogins})

def nurse(request):
    return render(request, "app/nurse.html")

def docsign(request):
    if request.method == "POST":
        docinstance = docregf(request.POST)
        if docinstance.is_valid():
            Username = docinstance.cleaned_data.get('Username')
            Password = docinstance.cleaned_data.get('Password')
            ConfirmPassword = docinstance.cleaned_data.get('ConfirmPassword')
            if Password == ConfirmPassword:
                User.objects.create_user(Username = Username, Password = Password)
                docinstance.save()
                return redirect('login')
            else:
                return redirect('pdm')
        else:
            return redirect('invalidf')
    else:
        docinstance = docregf()
        return render(request, "app/doc-signup.html", {"docinstance": docinstance})

def nursesign(request):
    return render(request, "app/nurse-signup.html")

def pdm(request):
    return render(request, "app/pdm.html")

def invalidf(request):
    return render(request, "app/invalid.hmtl")
