from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('logout/login/', views.userlogin, name='login'),
    path('home/', views.index, name='index'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup/user/', views.index, name='index'),
    path('user/', views.index, name='index'),
    path('login/user/', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
]