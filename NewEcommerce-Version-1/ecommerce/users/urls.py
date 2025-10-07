# Imports Django's built-in authentication views (login, logout, password reset, etc.)
from django.contrib.auth import views as auth_views

# Lets you create URL routes
from django.urls import path

# Imports views from this app to connect them to URLs
from . import views

# Imports LoginForm for Authentication from forms.py
from .forms import LoginForm

app_name = 'user' # Name sapce for the app


urlpatterns = [
    #  path('signup/', views.signup, name='signup'),

    # Uses the custom LoginForm for authentication and shows the login page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm), name='login'),

]