from django.urls import path, include
from .views import *

urlpatterns = [
    path('', store, name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', update_item, name="update_item"),
    path('process_order/', processOrder, name="process_order"),
]