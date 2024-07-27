from django.contrib import admin
from .models import ProductsList

class ProductsListAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductsList,ProductsListAdmin)
