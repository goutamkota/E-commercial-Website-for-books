from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    return render(request, 'bookstore/home.html')


def checkout(request):
    return render(request, 'bookstore/checkout.html')

def book_list(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/book_list.html', context)