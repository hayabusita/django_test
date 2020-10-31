from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={'id': self.id})