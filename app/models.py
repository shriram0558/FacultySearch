from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CollegeProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    profession = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    naac_rating = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")

class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    profession = models.TextField()
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    current_job = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    special_demand = models.TextField(blank=True, null=True)

class Jobcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(CollegeProfile, on_delete=models.CASCADE)
    dadeline = models.DateField()
    job_title = models.CharField(max_length=100, null=True)
    salary_range = models.CharField(max_length=100)
    job_description = models.TextField()
    stream = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    demands = models.TextField(null=True, blank=True)

class Application(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    college = models.ForeignKey(CollegeProfile, on_delete=models.CASCADE)
    jobcard = models.ForeignKey(Jobcard, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    