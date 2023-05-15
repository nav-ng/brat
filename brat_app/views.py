import uuid

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from brat_project.settings import EMAIL_HOST_USER
import datetime
from datetime import timedelta

# Create your views here.


def index(request):
    return render(request, 'index.html')


def s_register(request):
    if request.method == 'POST':
        a = sr_form(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['shop_name']
            ln = a.cleaned_data['shop_location']
            sd = a.cleaned_data['shop_id']
            em = a.cleaned_data['shop_email']
            ph = a.cleaned_data['shop_phone']
            ps = a.cleaned_data['shop_password']
            cp = a.cleaned_data['shop_c_password']
            if ps == cp:
                b = sr_model(shop_name=nm, shop_location=ln, shop_id=sd, shop_email=em, shop_phone=ph, shop_password=ps)
                b.save()
                return redirect(s_login)
            else:
                return HttpResponse("password not match")
        else:
            return HttpResponse("registration failed")
    return render(request, 'shop/shop_register.html')


def s_login(request):
    if request.method == 'POST':
        a = sl_form(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["shop_name"]
            ps = a.cleaned_data['shop_password']
            request.session['s_name'] = nm  # To make a variable global
            s = sr_model.objects.all()
            for i in s:
                if nm == i.shop_name and ps == i.shop_password:
                    request.session['sid'] = i.id
                    return redirect(sl_view)
            else:
                return HttpResponse("login failed")
    return render(request, 'shop/shop_login.html')


def sl_view(request):
    shop_name = request.session['s_name']
    return render(request, 'shop/sl_view.html', {'shop_name': shop_name})


def items_upload(request):
    shop_name = request.session['s_name']
    if request.method == 'POST':
        a = iu_form(request.POST, request.FILES)
        id = request.session['sid']
        if a.is_valid():
            pn = a.cleaned_data['product_name']
            pp = a.cleaned_data['product_price']
            pd = a.cleaned_data['product_description']
            pi = a.cleaned_data['product_image']
            b = iu_model(shop_id=id, product_name=pn, product_price=pp, product_description=pd, product_image=pi)
            b.save()
            return redirect(items_upload)
        else:
            return HttpResponse("upload failed")
    return render(request, 'shop/items_upload.html', {'shop_name': shop_name})


def item_edit(request, id):
    a = iu_model.objects.get(id=id)
    im = str(a.product_image).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES):
            if len(a.product_image) > 0:
                os.remove(a.product_image.path)
            a.product_image = request.FILES['product_image']
        a.product_name = request.POST.get('product_name')
        a.product_price = request.POST.get('product_price')
        a.product_description = request.POST.get('product_description')
        a.save()
        return redirect(posted_items_display)
    return render(request, 'shop/item_edit.html', {'a': a, 'im': im})


def item_delete(request, id):
    a = iu_model.objects.get(id=id)
    a.delete()
    return redirect(posted_items_display)


def posted_items_display(request):
    shop_name = request.session['s_name']
    s_id = request.session['sid']
    a = iu_model.objects.all()
    name = []
    price = []
    description = []
    image = []
    p_id = []
    shop_id = []
    for i in a:
        pn = i.product_name
        name.append(pn)
        pp = i.product_price
        price.append(pp)
        pd = i.product_description
        description.append(pd)
        pi = i.product_image
        image.append(str(pi).split('/')[-1])
        pid = i.id
        p_id.append(pid)
        sid = i.shop_id
        shop_id.append(sid)
    mylist = zip(name, price, description, image, p_id, shop_id)
    return render(request, 'shop/posted_items_display.html', {'mylist': mylist, 's_id': s_id, 'shop_name': shop_name})


def sample_home(request):
    a = iu_model.objects.all()
    name = []
    price = []
    description = []
    image = []
    p_id = []
    for i in a:
        pn = i.product_name
        name.append(pn)
        pp = i.product_price
        price.append(pp)
        pd = i.product_description
        description.append(pd)
        pi = i.product_image
        image.append(str(pi).split('/')[-1])
        pid = i.id
        p_id.append(pid)
    mylist = zip(name, price, description, image, p_id)
    return render(request, 'sample_home.html', {'mylist': mylist})


def sn(request):
    a = sn_model.objects.all()
    m_content = []
    m_date = []
    for i in a:
        mc = i.content
        m_content.append(mc)
        md = i.date
        m_date.append(md)
    mylist = zip(m_content, m_date)
    return render(request, 'shop/s_notification.html', {'mylist': mylist})


def u_register(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        email = request.POST.get('email')
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        password = request.POST.get('password')
        if User.objects.filter(username=u_name).first():  # it will get the first object from the filter query
            messages.success(request, 'username already taken')
            return redirect(u_register)
        if User.objects.filter(email=email).first():
            messages.success(request, 'email already exist')
            return redirect(u_register)
        user_obj = User(username=u_name, email=email, first_name=f_name, last_name=l_name)
        user_obj.set_password(password)
        user_obj.save()

        auth_token = str(uuid.uuid4())
        profile_obj = profile.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_function(email, auth_token)  # used-defined function
        return render(request, 'user/success.html')
    return render(request, 'user/user_register.html')


def send_mail_function(email, auth_token):
    subject = "your account has been verified"
    # f is a string literal which contain expressions inside curly brackets. the expressions are replaced by values.
    message = f'click link to verify your account http://127.0.0.1:8000/verify/{auth_token}'
    email_from = EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)  # build-in function


def verify(request, auth_token):
    profile_obj = profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request, 'your account is already verified')
            return redirect(u_login)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'your account has been verified')
        return redirect(u_login)
    else:
        messages.success(request, 'user not found')
        return redirect(u_login)


def u_login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=u_name).first()
        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect(u_login)
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified, check your email')
            return redirect(u_login)
        user = authenticate(username=u_name, password=password)
        if user is None:
            messages.success(request, 'wrong password or username')
            return redirect(u_login)
        request.session['u_nm'] = u_name
        request.session['uid'] = user_obj.id
        return redirect(home)
    return render(request, 'user/user_login.html')


def home(request):
    a = iu_model.objects.all()
    name = []
    price = []
    description = []
    image = []
    id = []
    for i in a:
        pn = i.product_name
        name.append(pn)
        pp = i.product_price
        price.append(pp)
        pd = i.product_description
        description.append(pd)
        pi = i.product_image
        image.append(str(pi).split('/')[-1])
        id1 = i.id
        id.append(id1)
    mylist = zip(name, price, description, image, id)
    return render(request, 'user/home.html', {'mylist': mylist})


def u_profile(request):
    username = request.session['u_nm']
    return render(request, 'user/u_profile.html', {'username': username})


def wishlist(request, id):
    u_id = request.session['uid']
    a = iu_model.objects.get(id=id)
    if wishlist_model.objects.filter(product_name=a.product_name):
        messages.success(request, 'Product is already in the wishlist')
        return redirect(home)
    else:
        b = wishlist_model(user_id=u_id, product_name=a.product_name, product_price=a.product_price,
                           product_description=a.product_description, product_image=a.product_image)
        b.save()
    return redirect(home)


def cart(request, id):
    u_id = request.session['uid']
    a = iu_model.objects.get(id=id)
    if cart_model.objects.filter(product_name=a.product_name):
        messages.success(request, 'Product is already in the Cart')
        return redirect(home)
    else:
        b = cart_model(user_id=u_id, product_name=a.product_name, product_price=a.product_price,
                       product_description=a.product_description, product_image=a.product_image)
        b.save()
    return redirect(home)


def wishlist_to_cart(request, id):
    u_id = request.session['uid']
    a = wishlist_model.objects.get(id=id)
    if cart_model.objects.filter(product_name=a.product_name):
        messages.success(request, 'product is already in the cart')
        return redirect(wishlist_display)
    else:
        b = cart_model(user_id=u_id, product_name=a.product_name, product_price=a.product_price,
                       product_description=a.product_description, product_image=a.product_image)
        b.save()
    return redirect(wishlist_display)


def wishlist_display(request):
    u_id = request.session['uid']
    a = wishlist_model.objects.all()
    name = []
    price = []
    description = []
    image = []
    id = []
    user_id = []
    for i in a:
        pn = i.product_name
        name.append(pn)
        pp = i.product_price
        price.append(pp)
        pd = i.product_description
        description.append(pd)
        pi = i.product_image
        image.append(str(pi).split('/')[-1])
        id1 = i.id
        id.append(id1)
        us_id = i.user_id
        user_id.append(us_id)
    mylist = zip(name, price, description, image, id, user_id)
    return render(request, 'user/wishlist.html', {'mylist': mylist, 'u_id': u_id})


def cart_display(request):
    u_id = request.session['uid']
    a = cart_model.objects.all()
    name = []
    price = []
    description = []
    image = []
    id = []
    user_id = []
    for i in a:
        pn = i.product_name
        name.append(pn)
        pp = i.product_price
        price.append(pp)
        pd = i.product_description
        description.append(pd)
        pi = i.product_image
        image.append(str(pi).split('/')[-1])
        id1 = i.id
        id.append(id1)
        us_id = i.user_id
        user_id.append(us_id)
    mylist = zip(name, price, description, image, id, user_id)
    return render(request, 'user/cart.html', {'mylist': mylist, 'u_id': u_id})


def wishlist_delete(request, id):
    a = wishlist_model.objects.get(id=id)
    a.delete()
    return redirect(wishlist_display)


def cart_delete(request, id):
    a = cart_model.objects.get(id=id)
    a.delete()
    return redirect(cart_display)


def buy(request, id):
    a = cart_model.objects.get(id=id)
    im = str(a.product_image).split('/')[-1]
    if request.method == 'POST':
        pn = request.POST.get('product_name')
        pp = request.POST.get('product_price')
        pq = request.POST.get('product_quantity')
        b = buy_model(product_name=pn, product_price=pp, product_quantity=pq)
        b.save()
        total_amount = int(pp) * int(pq)
        return render(request, "user/place_order.html", {'b': b, 'total_amount': total_amount})
    return render(request, 'user/buy.html', {'a': a, 'im': im})


def card(request):
    if request.method == 'POST':
        u_id = request.session['uid']
        card_holder_name = request.POST.get('card_holder_name')
        card_number = request.POST.get('card_number')
        date = request.POST.get('date')
        security_code = request.POST.get('security_code')
        user_obj = card_model(card_holder_name=card_holder_name, card_number=card_number, date=date,
                              security_code=security_code)
        user_obj.save()
        today = datetime.date.today()
        today += timedelta(days=10)
        a = User.objects.get(id=u_id)
        mail = a.email
        send_mail_func(mail, today)
        return render(request, 'user/order_summary.html', {'today': today})
    return render(request, 'user/payment_details.html')


def send_mail_func(mail, today):
    subject = "Order summary"
    message = f'Estimated arrival date is {today}'
    email_from = EMAIL_HOST_USER
    recipient = [mail]
    send_mail(subject, message, email_from, recipient)


def un(request):
    a = un_model.objects.all()
    m_content = []
    m_date = []
    for i in a:
        mc = i.content
        m_content.append(mc)
        md = i.date
        m_date.append(md)
    mylist = zip(m_content, m_date)
    return render(request, 'user/u_notification.html', {'mylist': mylist})
