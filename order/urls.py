from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('remove/<pk>',views.remove,name='remove'),
    path('confirm_order/',views.confirm_order,name='confirm_order'),
    path('orders/',views.orders,name='orders')
    
    
]
