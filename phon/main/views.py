from django.shortcuts import render
from django.views.generic import ListView, DetailView # Исправили импорт
from .models import Product

# 1. Добавляем IndexView (теперь Django его найдет)
class IndexView(ListView):
    model = Product
    template_name = 'main/catalog.html' # Твой файл с каталогом
    context_object_name = 'products'

# 2. Исправляем ProductDetailView (убираем DateDetailView)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

# Твою функцию product_list можно оставить, но IndexView сейчас важнее для работы сервера
def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/catalog.html', {'products': products})
