# from django.conf.urls import url
from django.urls import path, include
from .views import (
    BookListApiView,
)
from . import views

urlpatterns = [
    path('api/', BookListApiView.as_view()),
]