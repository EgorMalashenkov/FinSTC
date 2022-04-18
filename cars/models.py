from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_dealer = models.BooleanField(default=False)


class Car(models.Model):
    brand = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    dealer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="dealer"
    )
