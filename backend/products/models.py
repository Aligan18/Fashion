from django.db import models

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

MEN = 'M'
WOMEN = 'W'
GENDER_CHOICES = [
    (MEN, "Men"),
    (WOMEN, "Women"),
]


class Products(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to="photos/")
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.IntegerField(default=5, blank=True)
    favorite_count = models.IntegerField(default=0, blank=True)
    sale = models.IntegerField(default=0, blank=True)
    visible = models.BooleanField()

    def __str__(self):
        return self.title


class ProductInfo(models.Model):
    description = models.TextField()
    seo_text = models.TextField()
    products_info = models.ForeignKey("Products", on_delete=models.CASCADE)
