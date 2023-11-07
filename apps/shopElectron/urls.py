from django.urls import path

from apps.shopElectron.views import IndexViews,ProductViews
urlpatterns = [
    path('',IndexViews.as_view(),name='shop_electron_index'),
    path('<int:pk>/',ProductViews.as_view(),name="shop_electron_product")
]
