from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.colleges, name="index"),
    path('teachers', views.teachers, name="teachers"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('tdetail/<int:pk>', views.tdetail, name="tdetail"),
    path('handlesignup', views.handlesignup, name="handlesignup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
]
