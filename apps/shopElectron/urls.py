from django.urls import path

from apps.shopElectron.views import IndexViews,ProductViews,ProductDetailViews,ProductSummary
urlpatterns = [
    path('',IndexViews.as_view(),name='shop_electron_index'),
    path("product_summary/",ProductSummary.as_view(),name="product_summary"),
    path('<slug:slug>/',ProductViews.as_view(),name="shop_electron_product"),
    path('<slug:slug>/<int:pk>/',ProductDetailViews.as_view(),name="shop_product_detail")
]
