from django.contrib import admin

# Register your models here.
from .models import  Sale, SaleDetail, CarShop

admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.register(CarShop)