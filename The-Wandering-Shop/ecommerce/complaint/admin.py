from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'order_number', 'subject', 'created_at') #Shows key fields in list view in admin.
    list_filter = ('created_at',) #Adds filters by created_at in the sidebar.
    search_fields = ('name', 'email', 'order_number', ) #Allows searching by name, order, subject, or message.
    ordering = ('created_at',) #Orders complaints by most recent first.

# Register your models here.
