# Register your models here.
from django.contrib import admin

# Imports the models from models.py to register them with the admin site
from .models import Category, Product, Reviews

# Registers the Catergory model so it can be managed in the Django admin site
admin.site.register(Category)

# Registers the Product model so it can be managed in the Django admin site
admin.site.register(Product)

# Registers the Reviews model so it can be managed in the Django admin site
admin.site.register(Reviews)