# Generated by Django 4.2.1 on 2023-05-28 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comments_product_id_comments_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='user_id',
            new_name='user',
        ),
    ]