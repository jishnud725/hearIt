from django.shortcuts import render,redirect
from .models import order,orderItems
from product.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts')
def cart(request):
    user=request.user
    customer=user.user
    cart_obj,created=order.objects.get_or_create(
        owner=customer, 
        order_status=order.CART_STAGE
        )
    context={'cart':cart_obj}

    return render(request,'cart.html',context)


#add to cart
@login_required(login_url='accounts')
def add_to_cart(request):
    if request.POST:
        user=request.user
        quantity=int(request.POST.get("quantity"))
        customer=user.user
        product_id=request.POST.get("product_id")
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
        product_obj=product.objects.get(pk=product_id)

        orderItems_obj,created=orderItems.objects.get_or_create(
            product=product_obj,
            owner=cart_obj,
           
        )
        if created:
            orderItems_obj.quantity=quantity
            orderItems_obj.save()
        else:
            orderItems_obj.quantity=orderItems_obj.quantity+quantity
            orderItems_obj.save()

        
        return redirect('cart')
    


#remove from cart
@login_required(login_url='accounts')
def remove(request,pk):
    item=orderItems.objects.get(pk=pk)
    if item:
        item.delete()

    return redirect('cart')
    

# Confirm order
@login_required(login_url='accounts')
def confirm_order(request):
    if request.POST:
        user=request.user
        total=float(request.POST.get("total"))
        customer=user.user
        order_obj=order.objects.get(
            owner=customer,
            order_status=order.CART_STAGE
        )
        if order_obj:
            order_obj.order_status=order.ORDER_CONFIRMED
            order_obj.total=total
            order_obj.save()
            status_message='Order placed Successfully'
            messages.success(request,status_message)
        else:
            status_message='Problem while placing the order'
            messages.error(request,status_message)

    return redirect('orders')


#orders
@login_required(login_url='accounts')
def orders(request):
    user=request.user
    customer=user.user
    orders=order.objects.filter(owner=customer).exclude(order_status=order.CART_STAGE)
    context={'orders':orders}

    return render(request,'orders.html',context)