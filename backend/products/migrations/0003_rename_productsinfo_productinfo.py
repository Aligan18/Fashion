# Generated by Django 4.2.1 on 2023-05-29 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productsinfo_comments_remove_baskets_product_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsInfo',
            new_name='ProductInfo',
        ),
    ]