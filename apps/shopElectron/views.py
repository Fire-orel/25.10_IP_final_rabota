from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http.response import HttpResponseRedirect
from apps.shopElectron.models import Categorii,Product
from django.contrib.sessions.backends.db import SessionStore

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




# Create your views here.
