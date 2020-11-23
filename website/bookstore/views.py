import random
import string

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View


from users.models import Profile
from .models import Book, OrderItem, Order, Payment, Coupon, Refund, Address
from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

def home(request):
    return render(request, 'bookstore/home.html')


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


def book_list(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/book_list.html', context)

class ItemDetailView(DetailView):
    model = Book
    template_name = "bookstore/product-detail.html"



def checkout(request):

    return render(request, 'bookstore/checkout.html')


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")
