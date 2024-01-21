from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('logout/login/', views.userlogin, name='login'),
    path('home/', views.index, name='index'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('shop/', views.shop, name='shop'),
    path('shopservice/', views.shop_service, name='shop_service')
]