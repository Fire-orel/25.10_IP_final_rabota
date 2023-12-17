from typing import Any
from django.db import models
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
        print(request.session.session_key)
        # cart=Product.objects.create(user=user_id , product=product_id)
        return HttpResponseRedirect(redirect_to=".")

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



# Create your views here.
