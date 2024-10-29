from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import customer
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def accounts(request):
    if request.POST and 'register_button' in request.POST:
        try:
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            phone=request.POST.get("phone")
            address=request.POST.get("address")
            #creating user object
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            #creating customer object using user object

            customers=customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            return redirect('home')

        except Exception as e:
            error="Try Unique Username"
            messages.error(request,error)

    if request.POST and 'login_button' in request.POST:
        username=request.POST.get("username")
        password=request.POST.get("password")
      
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')



    return render(request,'accounts.html')


def sign_out(request):
    logout(request)
    return redirect('accounts')

