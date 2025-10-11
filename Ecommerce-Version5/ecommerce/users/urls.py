from django.urls import path

from .views import CustomLoginView

from . import views

from django.contrib.auth.views import LogoutView

app_name = 'users' # Name space for the app

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('customer-dashboard/', views.customer_dashboard, name='customer-dashboard'),
    path('profile/', views.profile_info, name='customer-dashboard'),
    

]




