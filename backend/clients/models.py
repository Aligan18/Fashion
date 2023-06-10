
from django.db import models

# Create your models here.
from custom_users.models import User
from products.models import Baskets


class Clients(models.Model):
    MEN = 'M'
    WOMEN = 'W'
    GENDER_CHOICES = [
        (MEN, "Men"),
        (WOMEN, "Women"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    order_count = models.IntegerField(default=0, blank=True)
    basket = models.ForeignKey(Baskets, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
