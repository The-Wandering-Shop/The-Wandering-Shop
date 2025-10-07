from django.urls import path

from .views import CustomLoginView

from . import views

from django.contrib.auth.views import LogoutView

app_name = 'user' # Name sapce for the app

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('customer-dashboard/', views.customer_dashboard, name='customer-dashboard'),
    

]

# urlpatterns = [
#     #  path('signup/', views.signup, name='signup'),

#     # Uses the custom LoginForm for authentication and shows the login page
#     path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm), name='login'),
    
# ]



