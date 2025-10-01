import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shirt', 'Shirt'),
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('socks', 'Socks'),
        ('ball', 'Ball'),
        ('short', 'Short'),
        ('jacket', 'Jacket'),
        ('hoodie', 'Hoodie'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='common')
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.brand
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()