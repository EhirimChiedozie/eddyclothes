from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='company_home'),
    path('about/', views.about, name='company_about'),
    path('cart/', views.cart, name='company_cart'),
    path('checkout/', views.checkout, name='company_checkout'),
    path('contact/', views.contact, name='company_contact'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/', views.product_detail, name='product_detail'),
]
