from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-created_at')[:10]
        return render(request, 'products/home.html', {'products':products})
    

class ProductsView(View):
    def get(self, request):
        return render(request, 'products/products.html')
    

class AboutUsView(View):
    def get(self, request):
        return render(request, 'products/about_us.html')