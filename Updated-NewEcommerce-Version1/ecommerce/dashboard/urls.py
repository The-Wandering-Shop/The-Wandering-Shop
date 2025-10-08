from django.urls import path
from . import views
from products.views import products

app_name = 'dashboard'

urlpatterns = [
    
    path('admin-dashboard/', views.dashboard, name='admin-dashboard'),  # Admin dashboard
    
    path('products/', products, name='products'),  # Shows all items (from item app)
    
    path('products/new/', views.new, name='new'),  # Page to create a new item
    
    path('products/<int:pk>/delete/', views.delete, name='delete'),

    path('products/<int:pk>/edit/', views.edit, name='edit'),

    
]
