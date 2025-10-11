from django.urls import path
from . import views

app_name = 'complaint'


urlpatterns = [
    path('', views.complaint_view, name='contact'), # root of app shows contact.html

]