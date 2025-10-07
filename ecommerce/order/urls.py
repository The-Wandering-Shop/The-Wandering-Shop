from django.urls import path
from . import views


urlpatterns = [
    path('wishlist/add/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('wishlist/remove/<int:pk>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:pk>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('my-selections/', views.user_selections, name='user_selections'),
 
]




