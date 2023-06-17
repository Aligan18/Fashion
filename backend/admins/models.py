from django.db import models
from django.dispatch import receiver
from djoser.signals import user_registered

from clients.models import Clients
from custom_users.models import User


class Admins(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    patronymic = models.CharField(max_length=80)

    def __str__(self):
        return self.surname


@receiver(user_registered, dispatch_uid="create_profile")
def create_profile(sender, user, request, **kwargs):
    """Создаём профиль пользователя при регистрации"""

    data = request.data

    if request.user.is_superuser:
        User.objects.filter(id=user.id).update(is_staff=True, is_active=True)
        Admins.objects.create(
            user=user,
            name=data.get("name", ""),
            surname=data.get("surname", ""),
            patronymic=data.get("patronymic", ""),

        )

    else:
        Clients.objects.create(

            user=user,
            name=data.get("name", ""),
            surname=data.get("surname", ""),
            patronymic=data.get("patronymic", ""),

        )
