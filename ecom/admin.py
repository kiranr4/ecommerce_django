from django.contrib import admin

# Register your models here.
from .models import Category, Brand, Product, ProductImage

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = ProductImageAdmin
    list_display = ["name", "product_image", "price"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category_image"]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)