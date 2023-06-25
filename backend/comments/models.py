from django.db import models

# Create your models here.
from custom_users.models import User
from products.models import Products


class Comments(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    user_name = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , blank=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
