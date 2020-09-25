from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField()