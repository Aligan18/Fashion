# Generated by Django 4.2.1 on 2023-06-25 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_clients_favorites_remove_clients_basket_and_more'),
        ('products', '0002_alter_baskets_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Baskets',
        ),
    ]
