from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import DenvalUserCreationForm, JuiceForm, FruitModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Juice, Cart, CartItem
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = DenvalUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('login')
    else:
        user_form = DenvalUserCreationForm()
    return render(request, 'denval_Juice/register.html', {'user_form': user_form})

#denval Home page

def home(request):
    return render(request, 'denval_Juice/home.html')


def menu(request):
    juices = Juice.objects.all().order_by('-id')
    return render(request, 'denval_Juice/menu.html', {'juices': juices})

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def add_juice(request):
    if request.method == 'POST':
        J_form = JuiceForm(request.POST, request.FILES)
        if J_form.is_valid():
            J_form.save()
            return redirect('denval_Juice:menu')
    else:
        J_form = JuiceForm()

    return render(request, 'denval_Juice/add_juice.html', {'J_form': J_form})

# Ensure every user has a cart on login
def get_user_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

@login_required
def add_to_cart(request, juice_id):
    juice = get_object_or_404(Juice, id=juice_id)
    cart = get_user_cart(request.user)
    
    # Check if the juice is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, juice=juice)
    
    if not created:
        cart_item.quantity += 1 
        cart_item.save()
    messages.success(request, f'You have successfully added { juice.name } costing {juice.price } to the cart')
    return redirect('denval_Juice:menu')

@login_required
def view_cart(request):
    cart = get_user_cart(request.user)
    items = cart.items.all()
    total_price = sum(item.get_total_price() for item in items)
    
    return render(request, 'denval_Juice/cart.html', {
        'cart': cart,
        'items': items,
        'total_price': total_price,
    })
    
#user payment
@login_required
def checkout(request):
    cart = get_user_cart(request.user)
    items = cart.items.all()
    total_price = sum(item.get_total_price() for item in items)
    
    # After checkout, clear the cart
    cart.items.all().delete()
    
    return render(request, 'denval_Juice/checkout.html', {
        'total_price': total_price
    })
    
def ownblend(request):
    fruit_variety = {
        'mango': 'mango',
        'orange': 'orange',
        'banana': 'banana',
        'pineapple': 'pineapple',
    }
    if request.method == 'POST':
        b_form = FruitModelForm(request.POST)
        if b_form.is_valid():
            b_form.save()
            messages.success(request, "Your preferred blend order has been received")
            return redirect('denval_Juice:menu')
    else:
        b_form = FruitModelForm()
    return render(request, 'denval_Juice/own_blend.html', {'b_form': b_form, 'fruit_variety': fruit_variety})

#user help

def help(request):
    return render(request, 'denval_Juice/help.html')