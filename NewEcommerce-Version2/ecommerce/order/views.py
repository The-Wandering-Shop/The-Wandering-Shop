from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from products.models import Product
from .models import Wishlistproduct
from .models import Cartproduct
from .models import Wishlistproduct, Cartproduct

# Adding to the wishlist.

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlistproduct.objects.get_or_create(user=request.user, product=product)
    return redirect('user_selections')

# Adding to the cart.
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_product, created = Cartproduct.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    return redirect('user_selections')

# User_selection(to displsy wishlist and cart).
@login_required
def user_selections(request):
    wishlist_products = Wishlistproduct.objects.filter(user=request.user)
    cart_products = Cartproduct.objects.filter(user=request.user)
    return render(request, 'order/user_selections.html', {
        'wishlist_products': wishlist_products,
        'cart_products': cart_products
    })

#Removing from Wishlist first section, second remove from cart.
@login_required
def remove_from_wishlist(request, pk):
    Wishlistproduct.objects.filter(pk=pk, user=request.user).delete()
    return redirect('user_selections')

@login_required
def remove_from_cart(request, pk):
    Cartproduct.objects.filter(pk=pk, user=request.user).delete()
    return redirect('user_selections')

#Update Cart Quantity
@login_required
def update_cart_quantity(request, pk):
    if request.method =='POST':
        cart_product = get_object_or_404(Cartproduct, pk=pk, user=request.user)
        quantity=int(request.POST.get('quantity'))
        cart_product.quantity = quantity
        cart_product.save()
    return redirect('user_selections')