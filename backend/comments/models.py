from django.db import models

# Create your models here.


class Comments(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    user_name = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.user_name

