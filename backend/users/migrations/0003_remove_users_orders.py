# Generated by Django 4.2.1 on 2023-05-29 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_comment_alter_users_basket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='orders',
        ),
    ]