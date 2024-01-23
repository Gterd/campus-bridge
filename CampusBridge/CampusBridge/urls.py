from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from product.views import product
from cart.views import checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('django.contrib.auth.urls')),
    path('__reload__/', include("django_browser_reload.urls")),
    path('shop/<slug:slug>/', product, name='product'),
    path('cart/', include('cart.urls')),
    path('checkout/', checkout, name='checkout'),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
