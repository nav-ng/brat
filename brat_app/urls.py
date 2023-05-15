from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('shop_register/', s_register),
    path('shop_login/', s_login),
    path('home/', home),
    path('sl_view/', sl_view),
    path('items_upload/', items_upload),
    path('posted_items_display/', posted_items_display),
    path('sample_home/', sample_home),
    path('item_edit/<int:id>', item_edit),
    path('item_delete/<int:id>', item_delete),
    path('user_register/', u_register),
    path('verify/<auth_token>', verify),
    path('user_login/', u_login),
    path('wishlist/<int:id>', wishlist),
    path('cart/<int:id>', cart),
    path('wishlist_display/', wishlist_display),
    path('cart_display/', cart_display),
    path('wishlist_delete/<int:id>', wishlist_delete),
    path('cart_delete/<int:id>', cart_delete),
    path('u_profile/', u_profile),
    path('buy/<int:id>', buy),
    path('payment_details/', card),
    path('wishlist_to_cart/<int:id>', wishlist_to_cart),
    path('s_notification/', sn),
    path('u_notification/', un)
]
