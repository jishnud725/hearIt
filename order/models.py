from django.db import models
from customer.models import customer
from product.models import product

# Create your models here.
class order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICE=(
        (ORDER_PROCESSED,"ORDER_PROCESSED"),
        (ORDER_DELIVERED,"ORDER_DELIVERED"),
        (ORDER_REJECTED,"ORDER_REJECTED")
    )
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True)
    total=models.FloatField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "order-{}".format(self.owner)



class orderItems(models.Model):
    product=models.ForeignKey(product,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name='added_items')




