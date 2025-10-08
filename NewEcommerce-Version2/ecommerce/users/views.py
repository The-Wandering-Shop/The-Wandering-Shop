from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView

from . forms import LoginForm, SignupForm

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return '/dashboard/admin-dashboard/'  
        return '/'
    
from django.shortcuts import render

# Imports the Item and Catergory models from the item app
from products.models import Category, Product



def index(request):
    """Homepage page view renders the homepage page template with unsold items and its categories."""
    # Gets the first 6 items that have not been sold
    products = Product.objects.all()

    # Gets  all available categories
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories, # Renders all the categories on the homepage
        'products':products, # Renders the the first 6 items that have not been sold on the homepage
    })

def signup(request):
    """Handles the user signup form and creates a new user."""

    if request.method == 'POST':
        # Checks if the form was submitted and creates a form with the submitted data
        form = SignupForm(request.POST)

        # Checks if the form is valid
        if form.is_valid():
            form.save()  # Saves the form and creates a new user

            return redirect('user:login') # Redirect to the login page after successful signup
    else:
        form = SignupForm() # Empty form and doesn't save

    return render(request, 'users/signup.html', {
        'form' : form # Renders the signup form
    })