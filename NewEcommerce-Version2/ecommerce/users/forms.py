# Imports Django form classes
from django import forms

# from .models import UserProfile

# Imports built-in forms for user signup and login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# # Imports Django's built-in User model
from django.contrib.auth.models import User

INPUT_CLASSES = "block w-full border border-gray-300 px-4 py-3 text-gray-600 text-sm rounded focus:ring-0  placeholder-gray-400"

class LoginForm(AuthenticationForm):
    """Custom login form to authenticate users."""

    username = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder' : 'Your username',
         'class' : INPUT_CLASSES,
     }))   
    
    # Password input with placeholder, Tailwind CSS styling, and built-in password validation
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder' : 'Your password',
         'class' : INPUT_CLASSES,
     }))


class SignupForm(UserCreationForm):
    """Custom signup form to create a new user account."""

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2') # Fields included in the form

    # Username input with placeholder, Tailwind CSS styling, and built-in text validation
    username = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder' : 'Your username',
         'class' : INPUT_CLASSES
     }))   
    
    # Email input with placeholder, Tailwind CSS styling, and built-in email validation
    email = forms.CharField(widget=forms.EmailInput(attrs={
         'placeholder' : 'Your email address',
         'class' : INPUT_CLASSES
     }))
    
    # Password input with placeholder, Tailwind CSS styling, and built-in password validation
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder' : 'Your password',
         'class' : INPUT_CLASSES
     }))
    
    # Password input with placeholder, Tailwind CSS styling, and built-in password validation to repeat pasword
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         'placeholder' : 'Repeat password',
         'class' : INPUT_CLASSES
     }))
    

    # class UserProfileForm(forms.ModelForm):
    #     class Meta:
    #         model = UserProfile
    #         fields = ['first_name', 'last_name', 'phone', 'birthday', 'gender']

    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #      'placeholder' : 'Your username',
    #      'class' : INPUT_CLASSES
    # }))   
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #      'placeholder' : 'Your username',
    #      'class' : INPUT_CLASSES
    # })) 
    # birthday = {
    #         'birthday': forms.DateInput(attrs={'type': 'date'}),
    #     }