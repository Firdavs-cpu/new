from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    akb = models.PositiveIntegerField(help_text='Акб')
    
    # 1. Создаем список вариантов памяти
    STORAGE_CHOICES = [
        (64, '64 GB'),
        (128, '128 GB'),
        (256, '256 GB'),
        (512, '512 GB'),
        (1024, '1 TB'),
    ]
    
    # 2. Меняем обычный IntegerField на поле с выбором (choices)
    storage = models.IntegerField(
        choices=STORAGE_CHOICES, 
        default=128, 
        help_text='Память'
    )
    
    color = models.CharField(max_length=50)
    CONDITION_CHOICES = [
        ('new', 'Новый'),
        ('ideal', 'Идеальное'),
        ('good', 'Хорошее'),
    ]
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='ideal')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='iphone_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.storage}GB)"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='iphone_photos/extra/')


    def __str__(self):
        return f"Фото для {self.product.name}"

