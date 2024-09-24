from django.shortcuts import render
from django.views import View
from .models import Product, Category
from django.db import models

# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-created_at')[:20]
        categories = Category.objects.annotate(product_count=models.Count('products'))[:5]
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'products/home.html', context)
    

class ProductsView(View):
    def get(self, request):
        return render(request, 'products/products.html')
    

class AboutUsView(View):
    def get(self, request):
        return render(request, 'products/about_us.html')