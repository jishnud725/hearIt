from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('accounts/',views.accounts,name='accounts'),
    path('logout/',views.sign_out,name='logout')
]
