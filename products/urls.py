from django.urls import path
from products import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), # Home page
    path('products/', views.ProductsView.as_view(), name='products'), # List of products page
    path('about_us/', views.AboutUsView.as_view(), name='about'),
]