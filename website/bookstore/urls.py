from django.urls import path
from . import views as store_views

urlpatterns = [
    path('', store_views.home, name='bookstore-home'),
    path('books/', store_views.book_list, name='book-list'),
    path('checkout/', store_views.checkout, name='checkout'),
    path('product/', store_views.ItemDetailView, name='product-detail')
]
