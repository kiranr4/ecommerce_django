# from django.contrib import admin

# # Register your models here.
# from .models import Category, Brand, Product, ProductImage

# class ProductImageAdmin(admin.TabularInline):
#     model = ProductImage


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImageAdmin]
#     list_display = ["name", "product_image", "price"]


# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ['name']


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category_image']






###########################################################################
###########################################################################

from django.contrib import admin
from .models import Brand, Category, Product, ProductImage

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'bid', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('bid',)  # Prevent editing auto-generated ID


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cid', 'name', 'category_image', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('cid',)  # Prevent editing auto-generated ID


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'pid', 'name', 'product_image', 'slug', 'category', 'brand', 'price', 'is_featured', 'is_popular', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'brand__name', 'category__name')
    readonly_fields = ('pid', 'slug')  # Prevent editing auto-generated ID and automatically generated slug
    autocomplete_fields = ('category', 'brand')  # Suggest related objects in dropdown
    # prepopulated_fields = {'slug': ('name',)}

    # def product_image(self, obj):
    #     return obj.product_image()


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('images', 'product', 'created_at', 'updated_at')
    # search_fields = ('product__name',)
    readonly_fields = ('created_at', 'updated_at')  # Images are uploaded, no need to edit timestamps

# Customize display for image fields
# admin.site.register([ProductImage], admin.StackedInlineAdmin(Product, fieldsets=[('Images', {'fields': ['images']})]))

# Customize admin title and header
admin.site.site_header = 'Divine Media House - Administration'
admin.site.site_title = 'DMH Admin'
