from django.urls import path
from products import views

urlpatterns = [
    path('', views.Home.as_view()) # Home page
]