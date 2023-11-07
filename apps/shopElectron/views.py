from django.shortcuts import render
from django.views.generic import ListView,DetailView

from apps.shopElectron.models import Categorii

class IndexViews(ListView):
    template_name='shop_electron/index.html'
    model=Categorii

class ProductViews(DetailView):
    template_name='shop_electron/products.html'
    model=Categorii

# Create your views here.
