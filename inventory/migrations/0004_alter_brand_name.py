# Generated by Django 4.1.5 on 2023-01-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
