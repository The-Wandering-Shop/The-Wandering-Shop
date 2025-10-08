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
        return '/users/customer-dashboard/'
    
@login_required
def customer_dashboard(request):
    return render(request, 'users/customer-dashboard.html')

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