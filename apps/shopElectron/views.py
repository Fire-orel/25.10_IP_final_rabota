from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from apps.shopElectron.models import Categorii,Product

class IndexViews(ListView):
    template_name='shop_electron/index.html'
    model=Categorii

class ProductViews(DetailView):
    template_name='shop_electron/products.html'
    model=Categorii

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
