from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/home.html', context)