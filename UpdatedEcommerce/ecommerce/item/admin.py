from django.contrib import admin

# Imports the models from models.py to register them with the admin site
from .models import Category, Item

# Registers the Catergory model so it can be managed in the Django admin site
admin.site.register(Category)

# Registers the Item model so it can be managed in the Django admin site
admin.site.register(Item)
