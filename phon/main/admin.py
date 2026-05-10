from django.contrib import admin
from .models import Product, ProductImage



class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 9


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'akb', 'storage', 'condition')
    search_fields = ('name', 'description')
    list_filter = ('condition', 'storage')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInLine]
    prepopulated_fields = { 'slug': ('name',)}




