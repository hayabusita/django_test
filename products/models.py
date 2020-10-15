from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField()

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'prod_id': self.id})