# Generated by Django 4.2.1 on 2023-05-27 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('seo_text', models.TextField()),
                ('comments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.comments')),
            ],
        ),
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
                ('products_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baskets.productsinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Baskets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='baskets.products')),
            ],
        ),
    ]
