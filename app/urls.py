from django.urls import path 
from . import views
urlpatterns = [
    path('', views.colleges, name="index"),
    path('teachers', views.teachers, name="teachers"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('tdetail/<int:pk>', views.tdetail, name="tdetail"),
    path('jobcarddetail/<int:pk>', views.jobcarddetail, name="jobcarddetail"),
    path('jobcardprofile/<int:pk>', views.jobcardprofile, name="jobcardprofile"),
    path('jobcardprofile/tdetail/<int:pk>', views.tdetail, name="tdetail"),
    path('jobcarddetail/apply/<int:pk>', views.apply, name="apply"),
    path('handlesignup', views.handlesignup, name="handlesignup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('search', views.search, name="search"),
    path('createcollegeprof', views.createcollegeprof, name="createcollegeprof"),
    path('createteacherprof', views.createteacherprof, name="createteacherprof"),
    path('yourprofile', views.yourprofile, name="yourprofile"),
    path('createjobcard', views.createjobcard, name="createjobcard"),
    path('jobcards', views.jobcards, name="jobcards"),
]
