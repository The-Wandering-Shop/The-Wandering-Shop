# Imports Django forms
from django import forms

# Imports the model Item models.py
from products.models import Product

# Tailwind CSS classes applied to all form fields for consistent styling
INPUT_CLASSES = 'w-full flex my-4 py-4 px-10 rounded-xl border border-black'

class NewItemForm(forms.ModelForm):
    """Form for creating a new item listing"""
    class Meta:
        model = Product # Connects the form to the Item model
        fields = ('category', 'name', 'description', 'price', 'image', 'is_new', 'quantity',) # Fields in the form

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
            'is_new' : forms.CheckboxInput(attrs={
            'class' : 'ml-2'
            }),
            'quantity' : forms.NumberInput(attrs={
            'class' : INPUT_CLASSES
            }),
        }

class EditItemForm(forms.ModelForm):
    """Lets the user edit the item listing"""
    class Meta:
        model = Product # Connects the form to the Item model
        fields = ('category','name', 'description', 'price', 'image', 'is_new', 'quantity',) # Fields that can be edited

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
            'is_new' : forms.CheckboxInput(attrs={
            'class' : 'ml-2'
            }),
            'quantity' : forms.NumberInput(attrs={
            'class' : INPUT_CLASSES
            }),
        }


