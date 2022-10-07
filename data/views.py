from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VolunteerDayForm , gadegetForm , reportForm , advertisementForm, CommentForm
# Create your views here.
from django.contrib.auth import get_user_model
from .models import VolunteerDay, Comment, report, gadeget, advertisement


Users=get_user_model()
def home(request):
    return render(request, 'mainAdmin.html')


def getAllUsers(request):
    users=Users.objects.all()
    return render(request, 'allUsers.html', {'users':users, 'title' :'allUsers'})


def getAllVolunteerDays(request):
    VolunteerDays=VolunteerDay.objects.all()
    return render(request, 'allVolunteerDays.html', {'VolunteerDays':VolunteerDays, 'title' :'VolunteerDays'})


def getAllGadgets(request):
    gadgets=gadeget.objects.all()
    return render(request, 'allgadgets.html', {'gadgets':gadgets, 'title' :'agadgets'})


def getAllCommments(request):
    comments=Comment.objects.all()
    return render(request, 'allComments.html', {'comments':comments, 'title' :'allcomments'})

def getAllAdvertisements(request):
    advertisements=advertisement.objects.all()
    return render(request, 'allAdvertisements.html', {'advertisements':advertisements, 'title' :'allAdvertisements'})

def getAllReports(request):
    reports=report.objects.all()
    return render(request, 'allReports.html', {'reports':reports, 'title' :'allReports'})

def getAllSupervisorsReports(request):
    users=Users.objects.all()
    return render(request, 'allUsers.html', {'users':users, 'title' :'allUsers'})
#=================================================  CREATE VIEWS ==================================================================


# THIS VEIW FOR ADDING NEW VOLUNTEER DAY IN THE DATABASE (ALL OTHER CREATE VIEWS HAVE THE SAME STRUCTURE )

# take request
def createVolunteerDay(request):
# if the method is post method ( when user is finish fulling  the form and click on create  )
    if request.method == 'POST':
        form = VolunteerDayForm(request.POST)
# the next line will return false if the user doesn,t enter the data  required or enter data from othe type
        if form.is_valid():
# if it return true we want to save entered data as a model object and go back to the home bage
            form.save()
            return HttpResponseRedirect(reverse('data:home'))

        else:
# if the a bove line return false we want it to return this line as htt response
            return HttpResponse('some data missed')


    else:
# when the method is get and not post we want it to return the next form

        form =VolunteerDayForm()
# this method is render by a user request and return as response the flowing html file with this form and this title
    return render(request, 'data/VolunteerDay.html', {'form': form, 'title' :'create Volunteer Day'})

def createGadeget(request):
    if request.method == 'POST':
        form = gadegetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('data:home'))

        else:
            return HttpResponse('some data missed')


    else:
        form =gadegetForm()
    return render(request, 'data/gadeget.html', {'form': form, 'title' :'create gadeget'})

def createReport(request):
    if request.method == 'POST':
        form = reportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('data:home'))

        else:
            return HttpResponse('some data missed')


    else:
        form =reportForm()
    return render(request, 'data/report.html', {'form': form, 'title' :'create report'})

def createAdvertisement(request):
    if request.method == 'POST':
        form = advertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('data:home'))

        else:
            return HttpResponse('some data missed')


    else:
        form =advertisementForm()
    return render(request, 'data/advertisement.html', {'form': form, 'title' :'create Volunteer Day'})

def createComment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('data:home'))

        else:
            return HttpResponse('some data missed')


    else:
        form =CommentForm()
    return render(request, 'data/comment.html', {'form': form, 'title' :'create comment'})
