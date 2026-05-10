from django.shortcuts import render
from django.views.generic import ListView, DetailView # Исправили импорт
from .models import Product

# 1. Добавляем IndexView (теперь Django его найдет)
class IndexView(ListView):
    model = Product
    template_name = 'main/catalog.html' # Твой файл с каталогом
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        storage_filter = self.request.GET.get('storage')
        condition_filter = self.request.GET.get('condition')

        if storage_filter:
            # Превращаем строку из URL в число, чтобы база данных поняла запрос
            queryset = queryset.filter(storage=int(storage_filter))
            
        if condition_filter:
            queryset = queryset.filter(condition=condition_filter)

        return queryset

    

# 2. Исправляем ProductDetailView (убираем DateDetailView)
class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

# Твою функцию product_list можно оставить, но IndexView сейчас важнее для работы сервера
def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/catalog.html', {'products': products})
