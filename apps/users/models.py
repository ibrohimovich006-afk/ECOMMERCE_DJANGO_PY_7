from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from apps.users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    phone_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    def __str__(self):
        return self.phone_number