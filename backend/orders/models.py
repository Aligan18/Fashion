
from django.db import models

# Create your models here.
from address.models import Addresses
from custom_users.models import User
from products.models import Products


class Orders(models.Model):
    NEW = "N"
    WORKING = "W"
    FINISHED = "F"
    STATUS_CHOICES = [
        (NEW, "New"),
        (WORKING, "Working"),
        (FINISHED, "Finished"),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=NEW, blank=True)
    county = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    user_name = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    address = models.ForeignKey(Addresses, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    order_info = models.ManyToManyField("OrderInfo")

    def __str__(self):
        return self.phone_number


class OrderInfo(models.Model):
    count = models.IntegerField()
    price_per_quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.PROTECT)
