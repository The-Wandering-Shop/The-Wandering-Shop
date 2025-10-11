from django import forms
from .models import Complaint
import re

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [ 'name', 'email', 'order_number', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
            'order_number': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-yellow-400'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-yellow-400',
                'rows': 4
            }),
        }


    def clean_name(self):
        name = self.cleaned_data['name']
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise forms.ValidationError("Name must contain only letters and spaces.")
        return name
    
    def clean_order_number(self):
        order_number = self.cleaned_data['order_number']
        if not order_number.isdigit():
            raise forms.ValidationError("Order number must be numeric.")
        if len(order_number) !=6:
            raise forms.ValidationError("Order number must be exactly 6 digits.")
        return order_number
    
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message.strip()) <10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
