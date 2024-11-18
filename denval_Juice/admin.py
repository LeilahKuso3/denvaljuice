from django.contrib import admin
from .models import Juice, CartItem, FruitModelForm


# Register your models here.
admin.site.register(Juice)
admin.site.register(CartItem)
# admin.site.register(Payment)
admin.site.register(FruitModelForm)
