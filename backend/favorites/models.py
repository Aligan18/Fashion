from django.db import models

# Create your models here.
from baskets.models import Products
from users.models import Users


class Favorites(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

