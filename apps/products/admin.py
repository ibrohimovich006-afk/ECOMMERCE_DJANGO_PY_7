from django.contrib import admin

from apps.products.models import Category, Product

admin.site.register(Product)
admin.site.register(Category)