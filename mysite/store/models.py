from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)\


    def __str__(self):
     return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
     return self.product_name

class Comment(models.Model):
    user = models.CharField(max_length=16)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f'{self.user} - {self.product}'