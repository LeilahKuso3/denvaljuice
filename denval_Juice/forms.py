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
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
        })
        
class JuiceForm(forms.ModelForm):
    class Meta:
        model = Juice
        fields = ('image','name', 'ml', 'price')
        
class FruitModelForm(forms.ModelForm):
    class Meta:
        model = FruitModelForm
        fields = ('name', 'blend_varieties')
   