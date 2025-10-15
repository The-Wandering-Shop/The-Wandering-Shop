# Imports Django forms
from django import forms

# Imports the model product models.py
from .models import Reviews

# Tailwind CSS classes applied to all form fields for consistent styling
INPUT_CLASSES = 'w-full my-4 py-4 px-10 rounded-xl border shadow-[0_0_10px_rgba(0,0,0,0.50)]'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'review', 'rating')
        widgets = {
            'name':forms.TextInput(attrs={
                'class': f'form-control {INPUT_CLASSES}',
                'id' : 'name'
            }),
            'email':forms.TextInput(attrs={
                'class': f'form-control {INPUT_CLASSES}',
                'id' : 'email'
            }),
            'review':forms.Textarea(attrs={
                'class':  f'form-control {INPUT_CLASSES}',
                'id' : 'review'
            }),
            'rating': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'id' : 'rating'
            })
        }