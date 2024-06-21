from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'company/home.html')

def about(request):
    return render(request, 'company/about.html')

def cart(request):
    return render(request, 'company/cart.html')

def checkout(request):
    return render(request, 'company/checkout.html')

def contact(request):
    return render(request, 'company/contact.html')

def my_account(request):
    return render(request, 'company/my_account.html')

def product_detail(request):
    return render(request, 'company/product_detail.html')

def product_list(request):
    return render(request, 'company/product_list.html')

def wishlist(request):
    return render(request, 'company/wishlist.html')