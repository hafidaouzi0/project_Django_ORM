from django.utils import timezone
from django.db import models





class Brand(models.Model):

    name=models.CharField(max_length=50)

    def __str__(self):
      return self.name



class ProductType(models.Model):
    name=models.CharField(max_length=255,unique=True)

    def __str__(self):
      return self.name

#a category can have one or many products
class Category(models.Model):
    name=models.CharField(max_length=100)
     
    def __str__(self):
      return self.name


# a product can have one and only category
class Product(models.Model):
   

    name=models.CharField(max_length=50)
    qty=models.IntegerField()
    price=models.DecimalField(max_digits=7,decimal_places=2,null=True)
    #date automatically generated when a product is created
    date_added=models.DateTimeField(auto_now_add=True,editable=False)
    #date automatically updated when a product is updated
    date_updated=models.DateTimeField(auto_now=True,null=True)
    url=models.SlugField(null=True)
    is_active=models.BooleanField(default=True)
    description=models.TextField(blank=True)
    #category=models.ForeignKey(Category,on_delete=models.CASCADE)
    #the relationship between the category and the product is many to many
    category=models.ManyToManyField(Category)



class Stock(models.Model):
  units=models.BigIntegerField()
  product=models.OneToOneField(Product,on_delete=models.CASCADE)