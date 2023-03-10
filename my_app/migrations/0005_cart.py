# Generated by Django 4.1.5 on 2023-02-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField()),
                ('product_description', models.CharField(max_length=200)),
                ('product_image', models.FileField(upload_to='')),
            ],
        ),
    ]
