from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from utils.models import UUIDBaseModel


class User(AbstractUser, PermissionsMixin):
    birth_date = models.DateField(null=True, blank=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    date_joined = models.DateField(null=True, blank=True)
    last_modified = models.DateField(null=True, blank=True)


class Employee(UUIDBaseModel, User):
    phone = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=100, null=False, default='', blank=True)
    state = models.CharField(max_length=140, null=False, default='', blank=True)
    city = models.CharField(max_length=140, null=False, default='', blank=True)
    neighborhood = models.CharField(max_length=100, null=False, default='', blank=True)
    zip_code = models.CharField(max_length=50, null=False, default='', blank=True)
    salary = models.FloatField(default=0.0)
