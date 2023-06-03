from django.db import models
from utils.models import UUIDBaseModel


class ProductType(UUIDBaseModel):
    type_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.type_name


class Product(UUIDBaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    buy_price = models.DecimalField(max_digits=5, decimal_places=2)
    sell_price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    catalog_id_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}  #{self.catalog_id_number}"
