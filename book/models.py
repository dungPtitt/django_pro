from django.db import models

# Create your models here.
class CategoryBook(models.Model):
  category_name = models.CharField(max_length=255)

class Author(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=255)

class Publisher(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=255)

class Book(models.Model):
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=255)
  # img = models.CharField(max_length=255)
  image = models.ImageField(null=True, blank=True)
  price = models.IntegerField()
  quantity = models.IntegerField()
  category = models.ForeignKey(CategoryBook, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authors")
  publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


