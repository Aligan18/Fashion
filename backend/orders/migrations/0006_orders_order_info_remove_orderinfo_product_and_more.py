# Generated by Django 4.2.1 on 2023-05-29 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productsinfo_comments_remove_baskets_product_and_more'),
        ('users', '0003_remove_users_orders'),
        ('orders', '0005_remove_orders_hello_alter_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_info',
            field=models.ManyToManyField(to='orders.orderinfo'),
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='product',
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.users'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.products'),
            preserve_default=False,
        ),
    ]