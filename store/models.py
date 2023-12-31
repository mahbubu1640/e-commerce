
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    size_or_weight = models.CharField(max_length=10)  # This field will dynamically switch between 'size' and 'weight'
    image = models.ImageField(upload_to='product_images/')
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
