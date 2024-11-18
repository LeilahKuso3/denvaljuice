from django.contrib import admin
from django.urls import path
from . import views


app_name = 'denval_Juice'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('add_juice/add/', views.add_juice, name='add-juice'),
    path('add-to-cart/<int:juice_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('makeblend/', views.ownblend, name='make-blend'),
    path('help/', views.help, name='help'),
    
    
]