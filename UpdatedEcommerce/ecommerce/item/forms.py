# Imports Django forms
from django import forms

# Imports the model Item models.py
from .models import Item

# Tailwind CSS classes applied to all form fields for consistent styling
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    """Form for creating a new item listing"""
    class Meta:
        model = Item # Connects the form to the Item model
        fields = ('category', 'name', 'description', 'price', 'image') # Fields in the form

        widgets = {
            'category' : forms.Select(attrs={
            'class' : INPUT_CLASSES
            }),
            'name' : forms.TextInput(attrs={
            'class' : INPUT_CLASSES
            }),
            'description' : forms.Textarea(attrs={
            'class' : INPUT_CLASSES
            }),
            'price' : forms.TextInput(attrs={
            'class' : INPUT_CLASSES
            }),
            'image' : forms.FileInput(attrs={
            'class' : INPUT_CLASSES
            }),
        }

class EditItemForm(forms.ModelForm):
    """Lets the user edit the item listing"""
    class Meta:
        model = Item # Connects the form to the Item model
        fields = ('name', 'description', 'price', 'image', 'is_sold') # Fields that can be edited

        widgets = {
            'name' : forms.TextInput(attrs={
            'class' : INPUT_CLASSES
            }),
            'description' : forms.Textarea(attrs={
            'class' : INPUT_CLASSES
            }),
            'price' : forms.TextInput(attrs={
            'class' : INPUT_CLASSES
            }),
            'image' : forms.FileInput(attrs={
            'class' : INPUT_CLASSES
            }),
        }