# Generated by Django 4.2.1 on 2023-06-09 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Men'), ('W', 'Women')], max_length=1)),
                ('type', models.CharField(choices=[('H', 'Головные уборы'), ('UB', 'Верх тела'), ('LB', 'Низ тела'), ('LG', 'Ноги'), ('UW', 'Белье')], max_length=2)),
                ('image', models.ImageField(upload_to='photos/')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField(blank=True, default=5)),
                ('favorite_count', models.IntegerField(blank=True, default=0)),
                ('sale', models.IntegerField(blank=True, default=0)),
                ('visible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('seo_text', models.TextField()),
                ('products_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='Baskets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(to='products.products')),
            ],
        ),
    ]
