from django.contrib import admin
from .models import Product, Category
from .forms import ProductForm

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'description',
        'region',
        'rating',
        'image',
        'price',
        'sku',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'type_product',
    )


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
