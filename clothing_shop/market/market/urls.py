"""
Proyecto Final
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path('', include('applications.box.urls')),
    # users app
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.favorite.urls')),
    # producto app
    re_path('', include('applications.product.urls')),
    # venta app
    re_path('', include('applications.sale.urls')),
    # caja app
    re_path('', include('applications.panel.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
