from django.db import models

# Create your models here.
from products.models import Baskets
from orders.models import Orders


class Users(models.Model):
    MEN = 'M'
    WOMEN = 'W'
    GENDER_CHOICES = [
        (MEN, "Men"),
        (WOMEN, "Women"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    order_count = models.IntegerField(default=0, blank=True)
    email = models.EmailField()
    basket = models.ForeignKey(Baskets, on_delete=models.PROTECT)
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
