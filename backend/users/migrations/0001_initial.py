# Generated by Django 4.2.1 on 2023-05-27 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('orders', '0001_initial'),
        ('baskets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Men'), ('W', 'Women')], max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('order_count', models.IntegerField(blank=True, default=0)),
                ('email', models.EmailField(max_length=254)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baskets.baskets')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comments')),
                ('orders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orders')),
            ],
        ),
    ]
