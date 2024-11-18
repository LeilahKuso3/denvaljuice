from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Juice(models.Model):
    image = models.ImageField(upload_to='juices/', default='default.jpg', blank=True, null=True)
    name = models.CharField(max_length=100)
    ml = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2) 
    
    def __str__(self):
        return self.name

#User to add items to the cart
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

#cart items themselves
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    juice = models.ForeignKey(Juice, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.juice.name}"

    def get_total_price(self):
        return self.quantity * self.juice.price
    
#user payment model
# class Payment(models.Model):
#     till_number = models.CharField(max_length=20)
#     amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
#     def __str__(self):
#          return f"TILL Number: {self.till_number}\nAmount: ksh{self.amount:.2f}"
     
#user create own blend
class FruitModelForm(models.Model):
    name = models.CharField(max_length=100)
    blend_varieties = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    