from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Juice, FruitModelForm

#denval user sign up form
class DenvalUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class JuiceForm(forms.ModelForm):
    class Meta:
        model = Juice
        fields = ('image','name', 'ml', 'price')

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ('till_number', 'amount')
        
class FruitModelForm(forms.ModelForm):
    class Meta:
        model = FruitModelForm
        fields = ('name', 'blend_varieties')
   