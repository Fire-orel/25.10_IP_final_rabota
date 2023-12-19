from django.urls import path

from apps.shopElectron.views import IndexViews,ProductViews,ProductDetailViews,ProductSummary,LoginViews,RegisterViews, logout
urlpatterns = [
    path('',IndexViews.as_view(),name='shop_electron_index'),
    path("product_summary/",ProductSummary.as_view(),name="product_summary"),
    path("login/",LoginViews.as_view(),name="login"),
    path("logout/",logout,name="logout"),
    path("register/",RegisterViews.as_view(),name="register"),
    path('<slug:slug>/',ProductViews.as_view(),name="shop_electron_product"),
    path('<slug:slug>/<int:pk>/',ProductDetailViews.as_view(),name="shop_product_detail")

]
