from django.db import models

from address.models import Addresses


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
    comment = models.ForeignKey("Comments", on_delete=models.CASCADE, blank=True, null=True)
    basket = models.ForeignKey("Baskets", on_delete=models.PROTECT)
    orders = models.ForeignKey("Orders", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    user_name = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.user_name


class Baskets(models.Model):
    product = models.ForeignKey("Products", on_delete=models.CASCADE, null=True)


class Orders(models.Model):
    NEW = "N"
    WORKING = "W"
    FINISHED = "F"
    STATUS_CHOICES = [
        (NEW, "New"),
        (WORKING, "Working"),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=NEW, blank=True)
    county = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    user_name = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    address = models.ForeignKey(Addresses, on_delete=models.PROTECT)

    def __str__(self):
        return self.phone_number


class Favorites(models.Model):
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    product = models.ForeignKey("Products", on_delete=models.CASCADE)


class OrderInfo(models.Model):
    count = models.IntegerField()
    price_per_quantity = models.IntegerField()
    product = models.ForeignKey("Products", on_delete=models.PROTECT)


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
    comments = models.ForeignKey("Comments", on_delete=models.CASCADE, null=True)
