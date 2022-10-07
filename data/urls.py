from django.contrib import admin
from django.contrib import auth
from django.urls import path
from . import views

app_name = "data"









urlpatterns = [
    path('',views.home, name ='home'),
    path('getAllUsers/', views.getAllUsers, name='getAllUsers'),
    path('getAllCommments/', views.getAllCommments, name='getAllCommments'),
    path('getAllReports/', views.getAllReports, name='getAllReports'),
    path('getAllSupervisorsReports/', views.getAllSupervisorsReports, name='getAllSupervisorsReports'),
    path('getAllAdvertisements/', views.getAllAdvertisements, name='getAllAdvertisements'), 
    path('getAllGadgets/', views.getAllGadgets, name='getAllGadgets'),
    path('getAllVolunteerDays/', views.getAllVolunteerDays, name='getAllVolunteerDays'),

    path('createVolunteerDay/', views.createVolunteerDay, name='createVolunteerDay'),
    path('createComment/', views.createComment, name='createComment'),
    path('createGadeget/', views.createGadeget, name='createGadeget'),
    path('createReport/', views.createReport, name='createReport'),
    path('createAdvertisement/', views.createAdvertisement, name='createAdvertisement'),

]
