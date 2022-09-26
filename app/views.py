from email.mime import application
from os import execv
from tokenize import Special
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Application, CollegeProfile, Faculty, Jobcard
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
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

def jobcarddetail(request, pk):
    college_detail = Jobcard.objects.get(id=pk)
    return render(request, "jobcarddetail.html", {'obj':college_detail})

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

def createcollegeprof(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            user = request.user
            description = request.POST.get('description')
            profession = request.POST.get('profession')
            naac_rating = request.POST.get('naac_rating')
            location = request.POST.get('location')
            email = request.POST.get('email')
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            if len(request.FILES) != 0:
                image = request.FILES['image']
            prod = CollegeProfile(name=name, address=address,description=description, image=image, user=user, profession=profession, naac_rating=naac_rating, location=location, email=email, contact=contact)
            prod.save()
            return redirect('/')
    return render(request, "createcollegeprof.html")

def handlelogout(request):
    logout(request)
    return render(request, "login.html")

def createteacherprof(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            user = request.user
            description = request.POST.get('description')
            profession = request.POST.get('profession')
            current_job = request.POST.get('current_job')
            speciality = request.POST.get('speciality')
            experience = request.POST.get('experience')
            special_demand = request.POST.get('special_demand')
            location = request.POST.get('location')
            email = request.POST.get('email')
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            if len(request.FILES) != 0:
                image = request.FILES['image']
            prod = Faculty(name=name, address=address,description=description, image=image, user=user, profession=profession, speciality=speciality, location=location,experience=experience, special_demand=special_demand, email=email, contact=contact)
            prod.save()
            return redirect('/')
    return render(request, "createteacherprof.html")

def createjobcard(request):
    user = request.user
    if user.is_authenticated:
        try:
            college = CollegeProfile.objects.get(user=request.user)
            if request.method == "POST":
                college = CollegeProfile.objects.get(user=user)
                job_title = request.POST.get('job_title')
                user = request.user
                salary_range = request.POST.get('salary_range')
                stream = request.POST.get('stream')
                speciality = request.POST.get('speciality')
                demands = request.POST.get('demands')
                job_description = request.POST.get('job_description')
                dadeline = request.POST.get('dadeline')
                prod = Jobcard(job_title=job_title, salary_range=salary_range, stream=stream, speciality=speciality, demands=demands, job_description=job_description, college=college, user=user,dadeline=dadeline)
                prod.save()
                return redirect('/')
        except:
            return redirect('/')
    return render(request, "createjobcard.html")

def yourprofile(request):
    try:
        profile_object = CollegeProfile.objects.get(user=request.user)
        applications = Jobcard.objects.filter(college=profile_object)
    except:
        return redirect('/')
    return render(request, "yourprofile.html", {'obj':profile_object, 'new_obj':applications})
def jobcards(request):
    jobcard_object = Jobcard.objects.all()
    return render(request, "jobcards.html", {'obj':jobcard_object})

def apply(request, pk):
    user = request.user
    if user.is_authenticated:
        jobcard_object = Jobcard.objects.get(id=pk)
        college = jobcard_object.college
        faculty = Faculty.objects.get(user=request.user)
        prod = Application(college=college, faculty=faculty, jobcard=jobcard_object)
        prod.save()
        return redirect('/')
    return render(request, "jobcards.html")

def jobcardprofile(request, pk):
    data = Jobcard.objects.get(id=pk)
    applicants = Application.objects.filter(college=data.college)
    return render(request, "jobcardprofile.html", {'obj':data, 'new_obj':applicants})

def search(request):
    query = request.GET['query']
    producttitle = CollegeProfile.objects.filter(Q(name__icontains=query)| Q(location__icontains=query))
    return render(request, "search.html", {'finalprod':producttitle})