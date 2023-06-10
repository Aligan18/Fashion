from django.db import models

# Create your models here.
from custom_users.models import User
from products.models import Products


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
