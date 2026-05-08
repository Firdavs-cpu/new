from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Эти колонки будут видны в списке всех товаров
    list_display = ('name', 'price', 'akb', 'storage', 'condition')
    # По этим полям можно будет искать
    search_fields = ('name', 'description')
    # Справа появится фильтр
    list_filter = ('condition', 'storage')
    # Автоматическое заполнение слага при вводе имени
    prepopulated_fields = {'slug': ('name',)}
