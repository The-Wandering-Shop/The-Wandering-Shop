# Imports Django's User model to authenticate and manage users 
from django.contrib.auth.models import User

# Imports Django's model classes to create database tables
from django.db import models


class Catergory(models.Model):
    """Lets you create categories for items, like Toys or Clothes."""

    # Input for the category name, maximum length 255 characters
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) # Orders the catergories alphabetically
        verbose_name_plural = 'Catergories'  #Displays plural name correctly in Django admin site

    def __str__(self):
        return self.name # Fixes string representataion problem and shows the catergory name in Django admin site instead of Catergory object(1)


class Item(models.Model):
    """Lets you create and manage items."""
    # Lets you choose which catergory the item belongs in 
    # related_name='items' : makes it easy to get all of the items belonging to a catergory
    # on_delete=models.CASCADE: if a category is deleted, all the items belonging to a catergory is also deleted
    catergory = models.ForeignKey(Catergory, related_name='items',on_delete=models.CASCADE)

    # Input for item name
    name = models.CharField(max_length=255)

    # Input for item description 
    description = models.TextField(blank=True, null=True)

    # Input for item price
    price = models.FloatField()

    # Input for image (Lets you add an image)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    # This allwos admin to put in stock quantity
    quatity = models.PositiveIntegerField(default=1)
    
    # Checkbox this is for new items of stock
    is_new = models.BooleanField(default=False)

    # Links the item with the user who created it using the ForeignKey
    # related_name='items' : makes it easy to get all of the items belonging to a specific user
    # on_delete=models.CASCADE: if the user is deleted, all their items are also deleted
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    # Automatically records date and time when the item was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name # Fixes string representataion problem and shows the item name in Django admin site instead of Item object(1)


