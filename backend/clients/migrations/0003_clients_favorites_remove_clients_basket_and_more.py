# Generated by Django 4.2.1 on 2023-06-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_baskets_product'),
        ('clients', '0002_remove_clients_email_remove_clients_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='favorites',
            field=models.ManyToManyField(related_name='clients_favorite', to='products.products'),
        ),
        migrations.RemoveField(
            model_name='clients',
            name='basket',
        ),
        migrations.AddField(
            model_name='clients',
            name='basket',
            field=models.ManyToManyField(blank=True, to='products.products'),
        ),
    ]
