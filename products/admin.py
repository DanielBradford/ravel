from django.contrib import admin
from .models import Product, Category, Color, Size

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class colorAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class sizeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)