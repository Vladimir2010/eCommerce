from django.contrib import admin
from .models import (Customer,
                     ProductsModel,
                     OrderModel,
                     OrderItemModel,
                     ShippingAddressModel)

# Register your models here.
admin.site.register(Customer)
admin.site.register(ProductsModel)
admin.site.register(OrderModel)
admin.site.register(OrderItemModel)
admin.site.register(ShippingAddressModel)