from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('update_item/', views.updateItem, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('process_order/', views.processOrder, name='process_order')
]
