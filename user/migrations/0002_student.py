# Generated by Django 4.1.5 on 2023-01-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54)),
                ('color', models.CharField(choices=[('RD', 'Red'), ('BL', 'Blue')], max_length=50)),
            ],
        ),
    ]
