from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.
from shop.models import Product
from .forms import AddProductForm
from .cart import Cart

def add(request,Product_id):
    cart = Cart(request)
    Product = get_object_or_404(Product, id=Product_id)

    form=AddProductForm(request.POST)

    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],is_update=cd['is_update'])

    return redirect('cart:detail')