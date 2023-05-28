from django.db import models

# Create your models here.

class Products(models.Model):
    MEN = 'M'
    WOMEN = 'W'
    GENDER_CHOICES = [
        (MEN, "Men"),
        (WOMEN, "Women"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    HEAD = 'H'
    UPPER_BODY = 'UB'
    LOWER_BODY = 'LB'
    LEGS = 'LG'
    UNDERWEAR = 'UW'
    TYPE_CHOICES = [
        (HEAD, "Головные уборы"),
        (UPPER_BODY, "Верх тела"),
        (LOWER_BODY, "Низ тела"),
        (LEGS, "Ноги"),
        (UNDERWEAR, "Белье"),
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to="photos/")
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.IntegerField(default=5, blank=True)
    favorite_count = models.IntegerField(default=0, blank=True)
    sale = models.IntegerField(default=0, blank=True)

    visible = models.BooleanField()
    products_info = models.ForeignKey("ProductsInfo", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProductsInfo(models.Model):
    description = models.TextField()
    seo_text = models.TextField()


class Baskets(models.Model):
    product = models.ManyToManyField("Products")

