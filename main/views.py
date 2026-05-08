from django.shortcuts import render
from .models import Product

def product_list(request):
    # Забираем все товары из базы
    products = Product.objects.all()
    # Отдаем их в шаблон
    return render(request, 'main/catalog.html', {'products': products})
