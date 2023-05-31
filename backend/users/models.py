from django.db import models

# Create your models here.
from products.models import Baskets


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

    def __str__(self):
        return self.name
