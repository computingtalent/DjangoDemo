from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=50, default="unknown")
    party = models.TextField(default="unknown")
    state = models.TextField(default="unknown")
    age = models.DecimalField(decimal_places=0, max_digits=3)
    sex = models.CharField(max_length=20)
    politician = models.BooleanField() 

class Host(models.Model):
    name = models.TextField()