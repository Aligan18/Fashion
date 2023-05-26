# Generated by Django 4.2.1 on 2023-05-23 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0002_alter_addresses_city_alter_addresses_county_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baskets',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='favorites',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='favorites',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderinfo',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='address_id',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='products_info_id',
            new_name='products_info',
        ),
        migrations.RenameField(
            model_name='productsinfo',
            old_name='comments_id',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='basket_id',
            new_name='basket',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='comment_id',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='orders_id',
            new_name='orders',
        ),
    ]