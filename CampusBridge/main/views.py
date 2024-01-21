from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.contrib.auth.decorators import login_required
from product.models import Product, Category
from django.db.models import Q
from service.models import College, Service, Service_Category

categories = Category.objects.all()
products = Product.objects.all()
universities = College.objects.all()
services = Service.objects.all()
category_services = Service_Category.objects.all()

footer_context = {
    'products': products,
    'Categories': categories,
}


def userlogin(request):
    if request.method == 'GET':
        print("User to be logged in")
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form, 'products': products,
                'Categories': categories,
                })
        
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
            return render(request, 'registration/login.html', {'form': form,'products': products,
                'Categories': categories,})
    else:
        form = LoginForm()
        print("User not logged in")
        return render(request, 'registration/login.html', {'form': form,'products': products,
                'Categories': categories,})



def userlogout(request):
    authlogout(request)
    return redirect('login/')

def index(request):
    context ={'products': products,
                'Categories': categories,
                }
    return render(request, 'main/index.html', context)

def signup(request):
    if request.method == 'GET':
        print("User to be created")
        form = RegisterForm()
        return render(request, 'registration/signup.html', {'form': form, 'products': products,
                'Categories': categories,})
        
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
            return render(request, 'registration/signup.html', {'form': form, 'products': products,
                'Categories': categories,})
    else:
        form = RegisterForm()
        print("User not created")
        return render(request, 'registration/signup.html', {'form': form, 'products': products,
                'Categories': categories,})

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
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

def shop_service(request):
    
    context = {
        'products': products,
        'Categories': categories,
        'universities': universities,
        'services': services,
        'category_services':category_services,
    }
    
    return render(request, 'main/shop_service.html', context)