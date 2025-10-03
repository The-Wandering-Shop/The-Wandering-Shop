from django.shortcuts import render

# Imports the Item and Catergory models from the item app
from item.models import Category, Item



def index(request):
    """Homepage page view renders the homepage page template with unsold items and its categories."""
    # Gets the first 6 items that have not been sold
    items = Item.objects.filter(is_sold=False)[0:6] 

    # Gets  all available categories
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories, # Renders all the categories on the homepage
        'items':items, # Renders the the first 6 items that have not been sold on the homepage
    })

