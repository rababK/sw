
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , get_user_model 
from django.shortcuts import render
from django.contrib import auth

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import  AccountCreationForm, SupervisorCreationForm ,AdminCreationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Users, supervisor

#################### index#######################################
def index(request):
    bestTowSupervisor= supervisor.objects.all()[:]
    if not request.user.is_authenticated:
        return render(request, 'index.html', {'title' :'index'})
    elif request.user.type==3:
    
        return render(request, 'volunteer.html', {'title' :'volunteer', 'best':bestTowSupervisor})
    elif request.user.type==1:
         return render(request, 'Admin.html', {'title' :'supervisor','best':bestTowSupervisor})
    elif request.user.type==2:
         return render(request, 'supervisor.html', {'title' :'admin','best':bestTowSupervisor})
    



########### register here #####################################
def volunteerRegister(request):
    print("______________________ ENTER 1_________________________")
    if request.method == 'POST':
        print("______________________ ENTER _________________________")
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password1')
            print(email, password)
            user = auth.authenticate(username=email, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('authentications:index'))
                return HttpResponse('Your id is inactive')
            return HttpResponse('Invalid login details provided')


    else:
        print("______________________ GET _________________________")
        form =AccountCreationForm()
    return render(request, 'Createvolunteeraccount.html', {'form': form, 'title' :'reqister here'})

def superviorRegister(request):
    if request.method == 'POST':
        form = SupervisorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email, password)
            user = auth.authenticate(username=email, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('authentications:index'))
                return HttpResponse('Your id is inactive')
            return HttpResponse('Invalid login details provided')


    else:
        form =SupervisorCreationForm()
    return render(request, 'user/register2.html', {'form': form, 'title' :'reqister here'})

def adminRegister(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            email = request.POST.get('email')
            password = request.POST.get('password1')
            print(email, password)
            user = auth.authenticate(username=email, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('authentications:index'))
                return HttpResponse('Your id is inactive')
            return HttpResponse('Invalid login details provided')


    else:
        form =AdminCreationForm()
    return render(request, 'user/register1.html', {'form': form, 'title' :'reqister here'})

################ login forms###################################################

def login(request):
    print("____________________enter")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = auth.authenticate(username=email, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                print("____________________done")
                return HttpResponseRedirect(reverse('authentications:index'))
            return HttpResponse('Your id is inactive')
        return HttpResponse('Invalid login details provided')


    context = {}
    return render(request, 'login.html', context=context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authentications:index'))

def getAllUsers(request):
    allusers=Users.objects.all()
    return render(request, 'allUsers.html', {'users': allusers, 'title' :'reqister here'})