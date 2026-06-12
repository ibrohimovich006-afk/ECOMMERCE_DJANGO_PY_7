from django.db import models
from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': str(self.price),
            'description': self.description,
            'category': self.category.name if self.category else None,
        }
       