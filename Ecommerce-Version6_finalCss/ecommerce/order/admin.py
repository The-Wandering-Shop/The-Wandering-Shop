from django.contrib import admin
from .models import Wishlistproduct, Cartproduct

@admin.register(Wishlistproduct)
# costomized the db for more functionality
class WishlistproductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at') #shows key fields in the admin list view.
    list_filter = ('added_at', 'user')              #Adds sidebar filter for date and user.
    search_fields = ('user__username', 'product__name') #Lets you search by username or product name.
    ordering = ('-added_at',) #Sorts entries by most recent first.

@admin.register(Cartproduct)
# customized the db for more functionality
class CartproductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at') #shows key fields in the admin list view.
    list_filter = ('added_at', 'user')              #Adds sidebar filter for date and user.
    search_fields = ('user__username', 'product__name') #Lets you search by username or product name.
    ordering = ('-added_at',) #Sorts entries by most recent first.

