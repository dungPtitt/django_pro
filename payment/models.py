from django.db import models
from cart.models import Cart

class Book(models.Model):
  date_payment = models.DateTimeField()
  method_payment = models.IntegerField()
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


