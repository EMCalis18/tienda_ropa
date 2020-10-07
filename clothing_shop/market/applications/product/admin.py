from django.contrib import admin

# Register your models here.
from .models import Product, Marca, SubCategoria, Category, Colors, Provider, Size, SizeNumber

admin.site.register(Product)
admin.site.register(Marca)
admin.site.register(SubCategoria)
admin.site.register(Category)
admin.site.register(Colors)
admin.site.register(Provider)
admin.site.register(Size)
admin.site.register(SizeNumber)