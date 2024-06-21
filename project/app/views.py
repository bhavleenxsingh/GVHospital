from django.shortcuts import render, redirect

# Create your views here.
from .forms import docregf, docloginf, nurseregf, nurseloginf, feedbackf, patientf
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import patientinfo, feedback


def home(request):
    return render(request, "app/home.html")

def faculty(request):
    return render(request, "app/faculty.html")

def docsign(request):
    if request.method == "POST":
        docinstance = docregf(request.POST)
        if docinstance.is_valid():
            UNI = docinstance.cleaned_data.get('Username')
            PI = docinstance.cleaned_data.get('Password')
            CPI = docinstance.cleaned_data.get('ConfirmPassword')
            if PI == CPI:
                user = User.objects.create_user(username = UNI, password = PI)
                user.save()
                docinstance.save()
                print("created")
                return redirect('success')
            else:
                print("pdm")
                return redirect('pdm')
        else:
            print("invalid")
            return redirect('invalidf')
    else:
        docinstance = docregf()
        return render(request, "app/doc-signup.html", {"docinstance": docinstance})

def doclog(request):
    if request.method == "POST":
        doclogins = docloginf(request.POST)
        if doclogins.is_valid():
            UIL = doclogins.cleaned_data.get('Username')
            PIL = doclogins.cleaned_data.get('Password')
            user = authenticate(request, username = UIL, password = PIL)
            if user is not None:
                auth_login(request, user)
                return redirect('dowhat')
            else:
                return redirect('dne')
        else:
            return redirect('invalidf')
    else:
        doclogins = docloginf()
        return render(request, "app/doctor.html", {"doclogins": doclogins})

# def nursesign(request):
#     if request.method == 'POST':
#         newnurse = nurseregf(request.POST)
#         if newnurse.is_valid():
#             Username = newnurse.cleaned_data.get('Username')
#             Password = newnurse.cleaned_data.get('Password')
#             ConfirmPassword = newnurse.cleaned_data.get('ConfirmPassword')
#             if Password == ConfirmPassword:
#                 User.objects.create_user(Username = Username, Password = Password)
#                 newnurse.save()
#                 return redirect('succcess')
#             else:
#                 return redirect('pdm')
#         else :
#             return redirect('invalidf')
#     else :
#         newnurse = nurseregf()
#         return render(request, "app/nurse-signup.html", {'newnurse': newnurse})

# def nurse(request):
#     if request.method =="POST":
#         nurselogin = nurseloginf(request.POST)
#         if nurselogin.is_valid():
#             Username = nurseloginf.cleaned_data.get('Username')
#             Password = nurseloginf.cleaned_data.get('Password')
#             user = authenticate(request, Username = Username, Password = Password)
#             if user is not None:
#                 auth_login(request, user)
#                 return redirect('dowhat')
#             else :
#                 return redirect("dne")
#         else:
#             return redirect('invalidf')
#     else:
#         nurselogin = nurseloginf()
#         return render(request, "app/nurse.html", {"nurselogin":nurselogin})

@login_required(login_url='doclog')
def addpatient(request):
    if request.method == "POST":
        newpatient = patientf(request.POST)
        if newpatient.is_valid():
            print(newpatient)
            newpatient.save()
            return redirect('success')
    else:
        newpatient = patientf()
    return render(request, "app/addpatient.html", {"newpatient": newpatient})

@login_required(login_url='doclog')
def patient(request):
    patientdetail = patientinfo.objects.all()
    return render(request, "app/patient.html", {"patientdetail":patientdetail})

def feedb(request):
    if request.method == 'POST':
        feed = feedbackf(request.POST)
        if feed.is_valid():
            feed.save()
            return redirect('success')
        else:
            return redirect('invalidf')
    else:
        feed = feedbackf()
        return render(request, "app/feedback.html", {'feed': feed})
    
@login_required(login_url='doclog')   
def viewfeedback(request):
    feedget = feedback.objects.all()
    return render(request, "app/viewfeedback.html", {'feedget': feedget})

def about(request):
    return render(request, "app/about.html")

def pdm(request):
    return render(request, "app/pdm.html")

def invalidf(request):
    return render(request, "app/invalid.html")

def dne(request):
    return render(request, "app/dne.html")

def success(request):
    return render(request, "app/success.html")

def dowhat(request):
    return render(request, "app/dowhat.html")

def logout(request):
    auth_logout(request)
    return render(request, "app/logout.html")

def edpat(request, id):
    getid = patientinfo.objects.get(id=id)
    gpi = patientf(instance = getid)
    if request.method == "POST":
        gpi = patientf(request.POST, instance = getid)
        if gpi.is_valid:
            gpi.save()
            return redirect("success")
        else:
            return redirect("invalidf")
    else :
        return render(request, "app/edit.html", {"gpi": gpi})
    
def delpat(request,id):
    deletep = patientinfo.objects.get(id = id)
    deletep.delete()
    return redirect('patient')

def cdel(request, id):
    patdelc = patientinfo.objects.get(id=id)
    delc = patientf(instance = patdelc)
    return render(request, "app/cdel.html", {"delc": delc, "patdelc": patdelc})