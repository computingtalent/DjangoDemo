# Generated by Django 2.1.7 on 2023-06-08 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_number',
            field=models.TextField(default=None),
        ),
    ]
