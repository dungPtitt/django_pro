# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
# from django.core import serializers

class BookListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        books = Book.objects.select_related().all()
        # books = Book.objects.filter()
        # author = books.author.all()
        # print(author)
        # books = Book.objects.prefetch_related('category', 'author', 'publisher').all()
        # books = Book.objects.raw("SELECT title, description FROM Book")
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'img': request.data.get('img'), 
            'price': request.data.get('price'), 
            'quantity': request.data.get('quantity'), 
            'category_id': request.data.get('category_id'), 
            'author_id': request.data.get('author_id'), 
            'publisher_id': request.data.get('publisher_id'), 
            # 'user': request.user.id
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @api_view(['PUT'])
    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        data = {
          'title': request.data.get('title'), 
          'description': request.data.get('description'), 
          'img': request.data.get('img'), 
          'price': request.data.get('price'), 
          'quantity': request.data.get('quantity'), 
          'category_id': request.data.get('category_id'), 
          'author_id': request.data.get('author_id'), 
          'publisher_id': request.data.get('publisher_id'), 
        }
        book = Book.objects.get(id = id)
        serializer = BookSerializer(instance=book, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        # id = request.DELETE.get('id')
        print(pk)
        book = Book.objects.get(id = pk)
        book.delete()
        return Response({"message": "Delete task success!"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def taskDelete(self, request, *args, **kwargs):
    id = request.DELETE.get('id')
    id = 1
    todo = Book.objects.get(id = id)
    todo.delete()
    return Response("Taks deleted successfully.", status=status.HTTP_200_OK)