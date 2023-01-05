from django.utils import timezone
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    qty=models.IntegerField()
    price=models.DecimalField(max_digits=7,decimal_places=2,null=True)
    #date automatically generated when a product is created
    date_added=models.DateTimeField(default=timezone.now)
    #date automatically updated when a product is updated
    date_updated=models.DateTimeField(auto_now=True,null=True)
    url=models.SlugField(null=True)
    is_active=models.BooleanField(default=True)

class Brand(models.Model):
    brand_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
      return self.name

class Category(models.Model):
    name=models.CharField(max_length=100)
