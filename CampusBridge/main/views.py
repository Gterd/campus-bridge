from django.shortcuts import render
from django.http import HttpResponse

def login(response):
    return render(response, 'main/login.html', {})
