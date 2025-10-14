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
                'class':'form-control',
                'class' : INPUT_CLASSES,
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'class' : INPUT_CLASSES,
            }),
            'review':forms.Textarea(attrs={
                'class':'form-control',
                'class' : INPUT_CLASSES,
            }),
            'rating': forms.Select(attrs={
                'class': INPUT_CLASSES,
            })
        }