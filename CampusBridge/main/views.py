from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login as authlogin, logout

def login(request):
    return render(request, 'registration/login.html', {})

def index(request):
    return render(request, 'main/index.html', {})

def signup(request):
    if request.method == 'GET':
        print("User to be created")
        form = RegisterForm()
        return render(request, 'registration/signup.html', {'form': form})
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("User is valid")
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')    
            new_user = authenticate(request, username=username, password=password)
            if new_user is not None:
                authlogin(request, new_user)
                print("User created")
                return redirect('home/')
                
    else:
        form = RegisterForm()
        print("User not created")
        return render(request, 'registration/signup.html', {'form': form})