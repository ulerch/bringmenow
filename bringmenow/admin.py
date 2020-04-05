from django.contrib import admin
from django.utils.html import format_html
from .models import Supplier, Product, Customer, Deliverer, Order, OrderItem


class SupplierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Supplier, SupplierAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)


class DelivererAdmin(admin.ModelAdmin):
    pass

admin.site.register(Deliverer, DelivererAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderItem, OrderAdmin)
