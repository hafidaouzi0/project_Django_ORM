from django.db import models

# Create your models here.



class Person(models.Model):
    FAV_COLOR=[
    ('RED','Red'),
    ('BLUE','Blue')
]
    name=models.CharField(max_length=54)
    color=models.CharField(max_length=50,choices=FAV_COLOR)

class Student(models.Model):

    class colors(models.TextChoices):
        RED='RD','Red'
        BLUE='BL','Blue'

    name=models.CharField(max_length=54)
    color=models.CharField(max_length=50,choices=colors.choices)
