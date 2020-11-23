from django.urls import path
from . import views as store_views

urlpatterns = [
    path('', store_views.home, name='bookstore-home'),
    path('books/', store_views.book_list, name='book-list'),
    path('checkout/', store_views.checkout, name='checkout'),
    path('product/<slug>/', store_views.ItemDetailView.as_view(), name='product-detail')
]
