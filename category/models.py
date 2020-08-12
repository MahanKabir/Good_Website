from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='static/images/category/')
