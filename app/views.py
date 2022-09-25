from email.mime import application
from os import execv
from tokenize import Special
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Application, CollegeProfile, Faculty, Jobcard
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def colleges(request):
    college_object = CollegeProfile.objects.all()
    return render(request, "colleges.html", {'obj':college_object})

def teachers(request):
    college_object = Faculty.objects.all()
    return render(request, "teachers.html", {'obj':college_object})

def detail(request, pk):
    college_detail = CollegeProfile.objects.get(id=pk)
    return render(request, "collagedetail.html", {'obj':college_detail})

def tdetail(request, pk):
    college_detail = Faculty.objects.get(id=pk)
    return render(request, "teacherdetail.html", {'obj':college_detail})

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #checks
        if len(username) > 10:
            return redirect('/handlesignup')
        if pass1 != pass2:
            return redirect('/handlesignup')
        #create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('/handlesignup')
    return render(request, "signup.html")

def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    return render(request, "login.html")

def handlelogout(request):
    logout(request)
    return redirect('/')