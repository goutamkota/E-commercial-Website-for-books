from django.shortcuts import render

# Create your views here.

def bookstore(request):
    return render(request, 'bookstore/bookstore.html')

def home(request):
    return render(request, 'bookstore/rough.html')
