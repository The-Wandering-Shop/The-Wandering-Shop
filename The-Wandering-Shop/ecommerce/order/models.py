from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Wishlistproduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} (Wishlist)"
    
class Cartproduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =models.PositiveBigIntegerField(default=1)
    added_at =models.DateTimeField(auto_now_add=True)

    @property
    def line_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.product.name} x{self.quantity} (Cart)"
    
