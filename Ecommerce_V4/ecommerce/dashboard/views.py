from django.contrib.auth.decorators import login_required

from django.utils.text import slugify

from django.shortcuts import render, get_object_or_404, redirect

from products.models import Category, Product, Reviews

from .forms import NewItemForm, EditItemForm


# Create your views here.
def dashboard(request):
    """Homepage page view renders the homepage page template with unsold items and its categories."""
    
    products = Product.objects.all()

    categories = Category.objects.all()

    return render(request, 'dashboard/admin-dashboard.html', {
        'categories': categories, 
        'products':products, 
    })

# Requires the user to be logged in before accessing this view
@login_required

def new(request):
    """View to create a new item listing."""

    products = Product.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            return redirect('dashboard:admin-dashboard')

    else:
        form = NewItemForm()

    return render(request, 'dashboard/form.html', {
        'form' : form,
        'title' : 'Add New Product'
    })

# Requires the user to be logged in before accessing this view
@login_required
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all() 
    
    old_category = product.category
    old_slug = product.slug
    old_name = product.name  # you can add other fields similarly
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            updated_product = form.save(commit=False)

            updated_product.slug = slugify(updated_product.name)

            if (old_category != updated_product.category or
                old_slug != updated_product.slug or
                old_name != updated_product.name):
                product.reviews.all().delete()

            updated_product.save()
            return redirect('dashboard:admin-dashboard')
    else:
        form = EditItemForm(instance=product)

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'Edit product',
        'product': product,
        'reviews': reviews,
        'edit': True
    })



# Requires the user to be logged in before accessing this view
@login_required

def delete(request, pk):
    """Allows the logged-in item owner to delete an item and redirects to the dashboard."""
    product = get_object_or_404(Product, pk=pk) # Gets item form database using the primary key
    reviews = product.reviews.all() 

    if request.method == 'POST':
        product.delete()
        return redirect('dashboard:admin-dashboard')

    return render(request, 'dashboard/delete-confirm.html', {
        'product': product,
        'reviews': reviews
        
        })
