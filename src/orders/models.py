from django.db import models

# Create your models here.
class Orders(models.Model):
    order_number = models.DecimalField(decimal_places=2,max_digits=1000)
    order_date = models.TimeField(default=None)
    shipped_date = models.TimeField(default=None)
    product_ordered = models.CharField(max_length=20)
    product_number=models.DecimalField(decimal_places=2,max_digits=1000)