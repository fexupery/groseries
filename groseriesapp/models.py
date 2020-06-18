from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='groseriesapp/images/', default='groseriesapp/images/default.png')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)
    presentation = models.CharField(max_length=100, blank=True)
    isBought = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null= True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.name + ' '+self.brand
