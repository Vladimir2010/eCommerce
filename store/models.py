from django.db import models
from django.contrib.auth.models import User


class CustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class ProductsModel(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True)

    # image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    #
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddressModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    zipcode = models.CharField(max_length=150, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address