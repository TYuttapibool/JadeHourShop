from django.shortcuts import render
from .models import * 
from django.http import JsonResponse
import json
from django.contrib import messages
from .models import *
from .utils import cookieCart, cartData

# Create your views here.

def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'home.html', context)

def product(request, product_id):
    data = cartData(request)
    cartItems = data['cartItems']

    one_product = Product.objects.get(id=product_id)
    products = Product.objects.all()
    context = {'product': one_product, 'products':products, 'cartItems': cartItems}
    return render(request, 'product.html', context)

def about(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'about.html', context)

def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'contact.html', context)

def shop(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'shop.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)

def updateItem(request): 
    data = json.loads(request.data)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete= False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)