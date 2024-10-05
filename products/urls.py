from django.urls import path
from products import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), # Home page
    path('products/', views.ProductsView.as_view(), name='products'), # List of products page
    path('about_us/', views.AboutUsView.as_view(), name='about'),
    path('number/', views.PhoneNumberView.as_view(), name='number'), # Get user number for announcements
    path('product/<int:product_id>/', views.ProductView.as_view(), name='product'), # Get user number for announcements
    path('product/<str:search_text>/', views.SearchProducts.as_view(), name='search'), # Search functionality
]