from re import A
from django.contrib import admin
from .models import CollegeProfile, Faculty, Jobcard, Application

# Register your models here.
admin.site.register(CollegeProfile)
admin.site.register(Faculty)
admin.site.register(Jobcard)
admin.site.register(Application)
