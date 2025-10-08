# Lets you create URL routes
from django.urls import path

# Imports views from this app to connect them to URLs
from . import views

app_name = 'item' # Name sapce for the app

urlpatterns = [
    path('', views.items, name='items'), # Shows all items 
    path('new/', views.new, name='new'), # Page to create a new item
    
    path('<int:pk>/delete/', views.delete, name='delete'), # Deletes a specific item
    path('<int:pk>/edit/', views.edit, name='edit'), # Edits a specific item
    
    path('<slug:category_name>/', views.items_by_category, name='items_by_category'),

    path('<slug:category_slug>/<slug:product_slug>/', views.detail, name='detail'), # Shows details of a specific item

]
