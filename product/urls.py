from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/',views.products, name='products'),
    path('product_details/<pk>',views.product_details,name='product_details'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')
    
]
