# Generated by Django 4.2 on 2023-05-18 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="buy_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=50)),
                ("product_price", models.IntegerField()),
                ("product_quantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="card_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("card_holder_name", models.CharField(max_length=50)),
                ("card_number", models.IntegerField()),
                ("date", models.CharField(max_length=50)),
                ("security_code", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="cart_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("product_name", models.CharField(max_length=50)),
                ("product_price", models.IntegerField()),
                ("product_description", models.CharField(max_length=200)),
                ("product_image", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="iu_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("shop_id", models.IntegerField()),
                ("product_name", models.CharField(max_length=50)),
                ("product_price", models.IntegerField()),
                ("product_description", models.CharField(max_length=200)),
                ("product_image", models.FileField(upload_to="brat_app/static")),
            ],
        ),
        migrations.CreateModel(
            name="sn_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="sr_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("shop_name", models.CharField(max_length=50)),
                ("shop_location", models.CharField(max_length=50)),
                ("shop_id", models.IntegerField()),
                ("shop_email", models.EmailField(max_length=254)),
                ("shop_phone", models.IntegerField()),
                ("shop_password", models.CharField(max_length=50)),
                ("shop_c_password", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="un_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=200)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="wishlist_model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("product_name", models.CharField(max_length=50)),
                ("product_price", models.IntegerField()),
                ("product_description", models.CharField(max_length=200)),
                ("product_image", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("auth_token", models.CharField(max_length=100)),
                ("is_verified", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
