from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.decorators import login_required
from product.models import product, Category
from django.db.models import Q

def userlogin(request):
    if request.method == 'GET':
        print("User to be logged in")
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("User is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')    
            user = authenticate(request, username=username, password=password)
            authlogin(request, user)
            print("User logged in")
            return redirect('index')
        else:
            form = LoginForm()
            print("User not created")
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
        print("User not logged in")
        return render(request, 'registration/login.html', {'form': form})



def userlogout(request):
    authlogout(request)
    return redirect('login/')

def index(request):
    products = product.objects.all()[0:8]
    return render(request, 'main/index.html', {'products': products})

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
            authlogin(request, new_user)
            print("User created")
            return redirect('user/')
        else:
            form = RegisterForm()
            print("User not created")
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = RegisterForm()
        print("User not created")
        return render(request, 'registration/signup.html', {'form': form})

def shop(request):
    categories = Category.objects.all()
    products = product.objects.all()
    
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__name=active_category)
    
    Query = request.GET.get('query', '')
    
    if Query:
        products = products.filter(Q(name__icontains=Query) | Q(description__icontains=Query))
    
    context = { 'products': products,
                'Categories': categories,
                'active_category': active_category
    }
    return render(request, 'main/shop.html', context)

