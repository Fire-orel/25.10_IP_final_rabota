from django.contrib import admin
from .models import Categorii,Product,Photo,Cart,Customers,Orders,Orders_detail

admin.site.register(Categorii)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(Cart)
admin.site.register(Customers)
class OrderDetailTabularInline(admin.TabularInline):

    model = Orders_detail
    extra = 0
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    inlines = [OrderDetailTabularInline]

# Register your models here.
