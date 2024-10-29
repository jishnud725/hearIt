from django.shortcuts import render
from . models import product
from django.core.paginator import Paginator
from customer.models import User

# Create your views here.

def index(request):
    featured_products=product.objects.order_by('priority')[:3]
    latest_products=product.objects.order_by('-id')[:3]
    

    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)

def products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=product.objects.all()
    product_paginator=Paginator(product_list,6)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)

def product_details(request,pk):
    product_for_description=product.objects.get(pk=pk)
    context={'product':product_for_description}

    return render(request,'product_details.html',context)


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')