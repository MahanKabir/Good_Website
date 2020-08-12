from django.db import models

# Create your models here.
from category.models import Category


class Blog(models.Model):
    name = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    price = models.CharField(max_length=10, null=True)
    page = models.CharField(max_length=4, null=True)
    image = models.ImageField(upload_to='static/images/blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)