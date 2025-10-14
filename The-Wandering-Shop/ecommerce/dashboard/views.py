from django.contrib.auth.decorators import login_required

from django.utils.text import slugify

from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404, redirect

from products.models import Category, Product, ProductDetail

from complaint.models import Complaint

from .forms import NewItemForm, EditItemForm, ProductDetailFormSet

from django.contrib.admin.views.decorators import staff_member_required

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
    """View to create a new item listing with product details."""
    
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        formset = ProductDetailFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            # Assign the product instance to each detail and save
            details = formset.save(commit=False)
            for detail in details:
                detail.product = product
                detail.save()
            # Handle any deleted forms if can_delete=True
            for obj in formset.deleted_objects:
                obj.delete()

            return redirect('dashboard:admin-dashboard')
    else:
        form = NewItemForm()
        formset = ProductDetailFormSet(queryset=ProductDetail.objects.none())  # empty formset for new product

    return render(request, 'dashboard/form.html', {
        'form': form,
        'formset': formset,
        'title': 'Add New Product',
    })


# Requires the user to be logged in before accessing this view
@login_required
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    old_category = product.category
    old_slug = product.slug
    old_name = product.name

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=product)
        formset = ProductDetailFormSet(request.POST, instance=product)
        
        if form.is_valid() and formset.is_valid():
            updated_product = form.save(commit=False)
            updated_product.slug = slugify(updated_product.name)

            if (old_category != updated_product.category or
                old_slug != updated_product.slug or
                old_name != updated_product.name):
                product.reviews.all().delete()

            updated_product.save()
            formset.save()  # formset linked to product instance

            return redirect('dashboard:admin-dashboard')
    else:
        form = EditItemForm(instance=product)
        formset = ProductDetailFormSet(instance=product)

    return render(request, 'dashboard/form.html', {
        'form': form,
        'formset': formset,
        'title': 'Edit product',
        'product': product,
        'reviews': reviews,
        'edit': True,
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

@staff_member_required
def all_users(request):
    users = User.objects.all()
    return render(request, 'dashboard/all-users.html', {'users': users})

staff_member_required
def customer_complaints(request):
    complaints = Complaint.objects.all()
    return render(request, 'dashboard/customer-complaints.html', {'complaints': complaints})