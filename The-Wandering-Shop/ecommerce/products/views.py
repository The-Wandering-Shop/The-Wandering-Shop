from django.contrib.auth.decorators import login_required

from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect

from django.http import Http404

from .models import Product, Category, Reviews

from .forms import ReviewForm


def products_by_category(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'products/products.html', {'products': products, 'category': category})


def products(request):
    """Displays all unsold products with optional filtering by category or search query."""
    query = request.GET.get('query','')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id) # Filter by selected category

    if query:
        # Filter products where name or description contains the search query
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'products/products.html',{
        'products' : products,
        'query' : query,
        'categories' : categories,
        'category_id' : int(category_id)
    })


def detail(request, category_slug, product_slug):
    """Displays details of an product and shows related products from the same category."""
    category = get_object_or_404(Category, slug=category_slug)
    
    product = Product.objects.filter(slug=product_slug, category=category).first()
    if not product:
        raise Http404("Product not found")
    
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[0:3]

    reviews = product.reviews.all()  # keep queryset in plural

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)   # use new variable
            new_review.product = product
            new_review.username = request.user
            new_review.save()
            form = ReviewForm(instance=new_review)
    else:
        form = ReviewForm()

    return render(request, 'products/detail.html', {
        'product': product,
        'reviews': reviews,  
        'form': form,
        'related_products': related_products,
    })



