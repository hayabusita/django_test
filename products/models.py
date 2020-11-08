from django.db import models
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField()

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'prod_id': self.id})