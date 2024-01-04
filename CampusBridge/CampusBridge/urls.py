from django.contrib import admin
from django.urls import path, include
from product.views import product
from cart.views import add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
    path('__reload__/', include("django_browser_reload.urls")),
    path('shop/<slug:slug>/', product, name='product'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
]
