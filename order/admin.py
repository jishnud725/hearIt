from django.contrib import admin
from .models import order,orderItems

# Register your models here.
admin.site.register(order)
admin.site.register(orderItems)