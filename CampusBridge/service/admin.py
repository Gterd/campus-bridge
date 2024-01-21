from django.contrib import admin
from .models import Service, Service_Category, College

admin.site.register(Service_Category)
admin.site.register(College)
admin.site.register([Service])