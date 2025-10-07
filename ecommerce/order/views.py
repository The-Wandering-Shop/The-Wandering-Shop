from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from item.models import Item
from .models import WishlistItem
from .models import CartItem
from .models import WishlistItem, CartItem

# Adding to the wishlist.

@login_required
def add_to_wishlist(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    WishlistItem.objects.get_or_create(user=request.user, item=item)
    return redirect('user_selections')

# Adding to the cart.
@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('user_selections')

# User_selection(to displsy wishlist and cart).
@login_required
def user_selections(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'order/user_selections.html', {
        'wishlist_items': wishlist_items,
        'cart_items': cart_items
    })

#Removing from Wishlist first section, second remove from cart.
@login_required
def remove_from_wishlist(request, pk):
    WishlistItem.objects.filter(pk=pk, user=request.user).delete()
    return redirect('user_selections')

@login_required
def remove_from_cart(request, pk):
    CartItem.objects.filter(pk=pk, user=request.user).delete()
    return redirect('user_selections')

#Update Cart Quantity
@login_required
def update_cart_quantity(request, pk):
    if request.method =='POST':
        cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
        quantity=int(request.POST.get('quantity'))
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('user_selections')