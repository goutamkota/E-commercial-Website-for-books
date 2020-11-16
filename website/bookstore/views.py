from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

books =[
    {
        'title': 'Brief answer to the big questions',
        'author': 'Stefen Hawking',
        'Highlights': ''
    }
]

def home(request):
    return render(request, 'bookstore/home.html')