# Register your models here.
from django.contrib import admin

# Imports the models from models.py to register them with the admin site
from .models import Category, ProductDetail, Product, Reviews

# Registers the Catergory model so it can be managed in the Django admin site
admin.site.register(Category)


# Add inline model for ProductDetail
class ProductDetailInline(admin.TabularInline):
    """ Enables table-style inline editing of ProductDetail inside
        the Product admin page
    """
    model = ProductDetail
    extra = 1
    can_delete = True

# register Product with the custom inline setup
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity', 'is_new']
    inlines = [ProductDetailInline]


# Registers the Reviews model so it can be managed in the Django admin site
admin.site.register(Reviews)