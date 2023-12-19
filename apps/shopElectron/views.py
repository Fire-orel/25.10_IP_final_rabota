from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,View
from django.http.response import HttpResponseRedirect
from apps.shopElectron.models import Categorii,Product,Customers
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect

class IndexViews(ListView):
    template_name='shop_electron/index.html'
    model=Categorii



class ProductViews(DetailView):
    template_name='shop_electron/products.html'
    model=Categorii





    def post(self , request, **kwargs):
        product_id=request.POST.get("product")
        # user_id=request.COOKIES['sessionid']
        cart = request.session.get('cart')
        if cart==None:
            request.session['cart'] = {}
            cart = request.session.get('cart')
        # print(cart)
        if product_id not in cart:
            cart[product_id] = 1

        else:
            cart[product_id]=cart[product_id]+1

        # print(request.session.items())
        # print(cart)

        request.session['cart'] = cart
        response=HttpResponseRedirect(redirect_to=".")
        return response

    def get_context_data(self, **kwargs):
        object_list=Categorii.objects.all()

        # products=Product.objects.all
        context=super().get_context_data(**kwargs,object_list=object_list)
        return context

class ProductDetailViews(DetailView):
    template_name='shop_electron/product_details.html'
    model=Product

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class ProductSummary(ListView):
    template_name="shop_electron/product_summary.html"
    model=Categorii
    def post(self , request, **kwargs):
        cart_check=request.POST.get('cart_check')
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        print(product,remove,cart)

        if cart_check:
            if remove:
                cart[product]-=1
            else:
                cart[product]+=1

        cart=dict(filter(lambda kv: kv[1] != 0, cart.items()))
        request.session['cart'] = cart
        response=HttpResponseRedirect(redirect_to=".")
        return response

    def get_context_data(self, *, object_list=None ,**kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.session.get("cart"))
        if self.request.session.get("cart")!=None:
            ids = list(self.request.session.get('cart').keys())
            count=self.request.session.get('cart')
            products = Product.get_products_by_id(ids)


            context["counts"]=count
            context["products"]=products
            # print(ids,products)
        return context

class LoginViews(ListView):
    template_name="shop_electron/login.html"
    model=Categorii
    def post(self , request, **kwargs):
        email=request.POST.get('email')
        password=request.POST.get('password')

        # print(email,password)

        data=Customers.get_customer_by_email_password(email,password)



        if data!=False:
            # print(type(data))
            print(data.email)
            request.session["customer"]=data.email

            response=HttpResponseRedirect(redirect_to="/")
            return response

        else:
            response=HttpResponseRedirect(redirect_to=".")
            return response


class RegisterViews(ListView):
    template_name="shop_electron/register.html"
    model=Categorii

    def post(self , request, **kwargs):
        last_name=request.POST.get("last_name")
        first_name=request.POST.get("first_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        date=request.POST.get("date")

        check_email=Customers.get_customer_by_email(email)
        if not check_email:
            customer=Customers(last_name=last_name,
                               first_name=first_name,
                               email=email,
                               password=password,
                               date_brith=date)
            customer.save()
            request.session["customer"]=email


            response=HttpResponseRedirect(redirect_to="/")
            return response
        else:
            response=HttpResponseRedirect(redirect_to=".")
            return response


def logout(request):
    del request.session["customer"]
    return redirect('login')
# Create your views here.
