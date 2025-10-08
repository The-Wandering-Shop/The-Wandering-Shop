# Makes sure a user must be logged in to access a view
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect

# Imports the NewItemForm and EditItemForm classes from forms.py
from .forms import NewItemForm, EditItemForm

# Imports the models Item and Catergory from models.py
from .models import Item, Catergory

def items_page(request):
    return render(request, 'item/items.html')

def items_by_category(request, category_name):
    category = get_object_or_404(Catergory, name__iexact=category_name)
    items = Item.objects.filter(catergory=category)
    return render(request, 'item/items.html', {'items': items, 'category': category})


def items(request):
    """Displays all unsold items with optional filtering by category or search query."""
    query = request.GET.get('query','')
    catergory_id = request.GET.get('catergory', 0)
    catergories = Catergory.objects.all()
    items = Item.objects.filter(is_sold=False)

    if catergory_id:
        items = items.filter(catergory_id=catergory_id) # Filter by selected category

    if query:
        # Filter items where name or description contains the search query
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html',{
        'items' : items,
        'query' : query,
        'catergories' : catergories,
        'catergory_id' : int(catergory_id)
    })


def detail(request, pk):
    """Displays details of an item and shows related items from the same category."""
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(catergory=item.catergory, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html',{
        'item' : item,
        'related_items' : related_items
    })

# Requires the user to be logged in before accessing this view
@login_required
def new(request):
    """View to create a new item listing."""
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form' : form,
        'title' : 'New item'
    })

# Requires the user to be logged in before accessing this view
@login_required
def edit(request, pk):
    """Allows the logged-in item owner to edit an item."""
    item = get_object_or_404(Item, pk=pk, created_by=request.user) # Lets the itme owner access the item

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item) # Form has an existing item

        # Checks if the fields are filled in correctly
        if form.is_valid():
            form.save() # Saves the editted form

            return redirect('item:detail', pk=item.id) 
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form' : form,
        'title' : 'Edit item'
    })

# Requires the user to be logged in before accessing this view
@login_required
def delete(request, pk):
    """Allows the logged-in item owner to delete an item and redirects to the dashboard."""
    item = get_object_or_404(Item, pk=pk, created_by=request.user) # Gets item form database using the primary key
    item.delete() # Deletes the item from the database

    return redirect('dashboard:index') # Redirects back to the dashboard
