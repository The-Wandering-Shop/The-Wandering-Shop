# Imports Django forms
from django import forms

from django.forms import inlineformset_factory

# Imports the model Item models.py
from products.models import Product

from products.models import ProductDetail

# Tailwind CSS classes applied to all form fields for consistent styling
INPUT_CLASSES = 'w-full my-2 py-2 px-4 rounded border border-black'

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


class ProductDetailForm(forms.ModelForm):
    class Meta:
        model = ProductDetail
        fields = ['label', 'value']
        widgets = {
            'label': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'value': forms.TextInput(attrs={'class': INPUT_CLASSES}),
        }

ProductDetailFormSet = inlineformset_factory(
    Product, 
    ProductDetail,
    form=ProductDetailForm,
    extra=3,
    can_delete=True
)