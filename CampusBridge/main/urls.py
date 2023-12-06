from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.index, name='index'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup')
]