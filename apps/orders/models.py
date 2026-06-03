from django.db import models

from django.contrib.auth.models import User
user = models.ForeignKey(User, on_delete=models.CASCADE)
address = models.TextField()
total_price = models.DecimalField(max_digits=10, decimal_places=2)