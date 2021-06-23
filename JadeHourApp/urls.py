from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product', views.product),
    path('about', views.about),
    path('contact', views.contact),
    path('shop', views.shop),
    path('cart', views.cart),
    path('checkout', views.checkout),
    path('update_item', views.updateItem),
    path('product/<int:product_id>', views.product),
]