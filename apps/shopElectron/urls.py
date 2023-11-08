from django.urls import path

from apps.shopElectron.views import IndexViews,ProductViews,ProductDetailViews
urlpatterns = [
    path('',IndexViews.as_view(),name='shop_electron_index'),
    path('<slug:slug>/',ProductViews.as_view(),name="shop_electron_product"),
    path('<slug:slug>/<int:pk>/',ProductDetailViews.as_view(),name="shop_product_detail")
]
