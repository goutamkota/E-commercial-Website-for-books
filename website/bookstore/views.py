from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    context = {
        'posts': Book.objects.all()
    }
    return render(request, 'bookstore/home.html', context)