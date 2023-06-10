
from django.db import models

from custom_users.models import User


class Addresses(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
