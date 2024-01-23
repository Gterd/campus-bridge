from django.shortcuts import render

def userprofile(request):
    
    context = {}
    
    return render(request, 'profiles/userprofile.html', context)

def vendorprofile(request):
    
    context = {}
    
    return render(request, 'profiles/vendorprofile.html', context)