from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class sr_model(models.Model):
    shop_name = models.CharField(max_length=50)
    shop_location = models.CharField(max_length=50)
    shop_id = models.IntegerField()
    shop_email = models.EmailField()
    shop_phone = models.IntegerField()
    shop_password = models.CharField(max_length=50)
    shop_c_password = models.CharField(max_length=50)

    def __str__(self):
        return self.shop_name


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class iu_model(models.Model):
    shop_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=200)
    product_image = models.FileField(upload_to='brat_app/static')

    def __str__(self):
        return self.product_name


class wishlist_model(models.Model):
    user_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=200)
    product_image = models.FileField()

    def __str__(self):
        return self.product_name


class cart_model(models.Model):
    user_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=200)
    product_image = models.FileField()

    def __str__(self):
        return self.product_name


class buy_model(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name


class card_model(models.Model):
    card_holder_name = models.CharField(max_length=50)
    card_number = models.IntegerField()
    date = models.CharField(max_length=50)
    security_code = models.IntegerField()

    def __str__(self):
        return self.card_holder_name


class sn_model(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)


class un_model(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

