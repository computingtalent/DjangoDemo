from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    product_number = models.DecimalField(decimal_places=2,max_digits=1000)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    summary = models.TextField()
    in_stock = models.BooleanField()
