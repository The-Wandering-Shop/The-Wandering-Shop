from django.urls import path

from . import views

app_name = 'product' # Name sapce for the app


urlpatterns = [
    path('', views.products, name='products'), # Shows all products 
    
    path('<slug:category_name>/', views.products_by_category, name='products_by_category'),

    path('<slug:category_slug>/<slug:product_slug>/', views.detail, name='detail'), # Shows details of a specific product

]
