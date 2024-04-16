from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  shop_order_id = models.IntegerField(default=0)
  transaction_id = models.IntegerField(default=0)
  complete = models.BooleanField(default=False)

  @property
  def shipping(self):
    shipping = False
    cartitems = self.cartitem_set.all()
    for i in cartitems:
        if i.book.category:
          shipping = True
    return shipping
  
  @property
  def get_cart_total(self):
    cartitems = self.cartitem_set.all()
    total = sum([item.get_total for item in cartitems])
    return total
  @property
  def get_cart_items(self):
    cartitems = self.cartitem_set.all()
    total = sum([item.quantity for item in cartitems])
    return total

class CartItem(models.Model):
  quantity = models.IntegerField(default=0)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  @property
  def get_total(self):
    total = self.quantity*self.book.price
    return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address