from django import forms


class sr_form(forms.Form):
    shop_name = forms.CharField(max_length=50)
    shop_location = forms.CharField(max_length=50)
    shop_id = forms.IntegerField()
    shop_email = forms.EmailField()
    shop_phone = forms.IntegerField()
    shop_password = forms.CharField(max_length=50)
    shop_c_password = forms.CharField(max_length=50)


class sl_form(forms.Form):
    shop_name = forms.CharField(max_length=50)
    shop_password = forms.CharField(max_length=50)


class ul_form(forms.Form):
    user_name = forms.CharField(max_length=50)
    user_password = forms.CharField(max_length=50)


class iu_form(forms.Form):
    product_name = forms.CharField(max_length=50)
    product_price = forms.IntegerField()
    product_description = forms.CharField(max_length=200)
    product_image = forms.FileField()


class card_form(forms.Form):
    card_holder_name = forms.CharField(max_length=50)
    card_number = forms.IntegerField()
    date = forms.CharField(max_length=50)
    security_code = forms.IntegerField()
