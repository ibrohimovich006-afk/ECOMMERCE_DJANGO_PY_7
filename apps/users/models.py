from django.db import models
from apps.common.models import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username