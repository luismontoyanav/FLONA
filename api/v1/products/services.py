from products.models import Product, ProductType
from django.core.exceptions import ObjectDoesNotExist
from typing import Union
from uuid import UUID


def get_product_by_type(product_type: int):
    products = Product.objects.filter(product_type_id=product_type)
    return products


def get_all_products():
    products = Product.objects.all()
    return products


def get_product_types():
    product_types = ProductType.objects.all()
    return product_types


def get_product_type_by_id(product_type_id: int):
    try:
        return ProductType.objects.get(id=product_type_id)
    except ObjectDoesNotExist:
        return None


def get_product_type_by_type_name(product_type_name: str):
    try:
        return ProductType.objects.get(type_name=product_type_name)
    except ObjectDoesNotExist:
        return None


def get_product_type_by_uuid(product_type_uuid: Union[UUID, str]):
    try:
        return ProductType.objects.get(uuid=product_type_uuid)
    except ObjectDoesNotExist:
        return None
