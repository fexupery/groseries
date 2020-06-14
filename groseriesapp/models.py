from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    presentation = models.CharField(max_length=100)
    isBought = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null= True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name + ' '+self.brand
