from django.db import models

# Create your models here.
from products.models import Products
from users.models import Users


class Comments(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    user_name = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

