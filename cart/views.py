from django.shortcuts import render
from .models import CartItem, Cart, ShippingAddress
from book.models import Book
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
# Create your views here.

def cart(request):
    if(request.user.is_authenticated):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
    else:
        items=[]
        cart = {"get_cart_total": 0}
    print("items", items)
    context = {
        'items': items,
        'cart': cart
    }
    return render(request, 'cart.html', context)

# @api_view(['POST'])
def updateItem(request):
    data = json.loads(request.body)
    # data = request.data
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, complete=False)
    # print("user", user)
    action = data["action"]
    productId = data["productId"]
    book = Book.objects.get(id=productId)
    # print("book", book)
    cartItem, created = CartItem.objects.get_or_create(book=book, cart=cart)
    if(action=="add"):
        cartItem.quantity = cartItem.quantity+1
    elif action=="remove":
        cartItem.quantity = cartItem.quantity-1
    cartItem.save()
    if cartItem.quantity<=0:
        cartItem.delete()
    # print("dadas,a")
    return JsonResponse("Item was added", safe=False)

# @api_view(['POST'])
def checkout(request):
    if(request.user.is_authenticated):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        items = cart.cartitem_set.all()
    else:
        items=[]
        cart = {"get_cart_total": 0}
    print("items", items)
    context = {
        'items': items,
        'cart': cart
    }
    return render(request, 'checkout.html', context)

# @api_view(['POST'])
def processOrder(request):
    data = request.body
    print("Data: ", data)
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user, complete=False)
        cart.complete = True
        cart.save()

        # ShippingAddress.objects.create(
        #     customer=user,
        #     order=cart,
        #     address=data['shipping'['address']],
        #     city=data['shipping'['city']],
        #     state=data['shipping'['state']],
        #     zipcode=data['shipping'['zipcode']],
        # )
    else:
        print("User is not login!")
    return JsonResponse("Item was added", safe=False)