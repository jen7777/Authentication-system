from django.shortcuts import render
from .models import signup
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method == 'POST':

        username=request.POST.get('username')                           #adding recieved name to new variable username
        firstname=request.POST.get('firstname') 
        lastname=request.POST.get('lastname')                    
        password1=request.POST.get('password1')
        
        myuser=User.objects.create_user(username,email,password1)       #creating new object myuser for inbuilt model class Users
        myuser.first_name = firstname                                   #adding variables using object myuser 
        myuser.last_name = lastname
        
        myuser.save()    
    return render(request,'signup.html')
def signin(request):
    return render(request,'signin.html')