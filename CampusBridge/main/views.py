from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login as authlogin, logout

def login(request):
    return render(request, 'registration/login.html', {})

def index(request):
    return render(request, 'main/index.html', {})

def signup(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print("User is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                authlogin(request, new_user)
                redirect('home/')
                print("User created")
    form = RegisterForm()
    print("User not created")
    return render(request, 'registration/signup.html', {'form': form})