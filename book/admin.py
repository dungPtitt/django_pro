from django.contrib import admin
from .models import Book, CategoryBook, Author, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(CategoryBook)
admin.site.register(Author)
admin.site.register(Publisher)
