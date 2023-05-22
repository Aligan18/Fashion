from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    order_count = models.IntegerField()
    is_man = models.BooleanField()
    email = models.CharField(max_length=100)
    comment_id = models.ForeignKey("Comments", on_delete=models.CASCADE)
    basket_id = models.ForeignKey("Baskets", on_delete=models.PROTECT)
    orders_id = models.ForeignKey("Orders", on_delete=models.CASCADE)


class Comments(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    user_name = models.CharField(max_length=100)
    text = models.TextField(blank=True)


class Baskets(models.Model):
    product_id = models.ForeignKey("Products", on_delete=models.CASCADE)


class Orders(models.Model):
    county = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    user_name = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    status = models.IntegerField()
    address_id = models.ForeignKey("Addresses", on_delete=models.PROTECT)


class Favorites(models.Model):
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Products", on_delete=models.CASCADE)


class OrderInfo(models.Model):
    count = models.IntegerField()
    price_per_quantity = models.IntegerField()
    product_id = models.ForeignKey("Products", on_delete=models.PROTECT)


class Addresses(models.Model):
    county = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)


class Products(models.Model):
    image = models.ImageField(upload_to="photos/")
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    rating = models.IntegerField(default=5)
    favorite_count = models.IntegerField(default=0)
    sale = models.IntegerField(default=0)
    for_man = models.BooleanField()
    type = models.CharField(max_length=100)
    visible = models.BooleanField()
    products_info_id = models.ForeignKey("ProductsInfo", on_delete=models.CASCADE)


class ProductsInfo(models.Model):
    description = models.TextField()
    seo_text = models.TextField()
    comments_id = models.ForeignKey("Comments", on_delete=models.CASCADE)





