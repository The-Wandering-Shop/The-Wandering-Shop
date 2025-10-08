from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path('core/', include('core.urls')),
    path('products/', include('products.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('order/', include('order.urls')),
    
    # path("theme1/", theme1, name="theme1"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)