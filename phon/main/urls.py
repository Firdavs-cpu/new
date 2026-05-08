# main/urls.py
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # Маршрут для карточки товара:
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
