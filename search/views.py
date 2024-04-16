from django.shortcuts import render
from book.models import Book
from django.db.models import Q

# Create your views here.


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(title__icontains=q) | Q(description__icontains=q))
        data = Book.objects.filter(multiple_q)
    else:
        data = Book.objects.all()
    context = {
        'data': data
    }
    print("data", data)
    return render(request, 'index.html', context)