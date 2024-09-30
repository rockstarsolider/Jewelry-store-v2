from django.shortcuts import render, get_object_or_404  
from django.views import View
from .models import Product, Category
from django.db import models
from .forms import PhoneNumberForm  
from .models import PhoneNumber

# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all().order_by('-created_at')[:20]
        categories = Category.objects.annotate(product_count=models.Count('products'))[:5]
        context = {
            'products': products,
            'categories': categories,
            'form': PhoneNumberForm()
        }
        return render(request, 'products/home.html', context)
    

class ProductsView(View):
    def get(self, request):
        return render(request, 'products/products.html')
    

class AboutUsView(View):
    def get(self, request):
        return render(request, 'products/about_us.html')
    

# Detail of a product
class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'products/product.html', {'product': product})


class PhoneNumberView(View):
    def get(self, request):
        form = PhoneNumberForm()
        return render(request, 'home/phone_number_form.html', {'form': form})  
    
    def post(self, request):
        form = PhoneNumberForm(request.POST)  
        if form.is_valid():   
            PhoneNumber.objects.create(phone_number=form.cleaned_data['phone_number'])  
            message = "فرم با موفقیت ثبت شد"  
            return render(request, 'home/phone_number_form.html', {'message': message, 'form': form}) 
        else:
            message = 'شماره تلفن باید حداقل 11 رقم باشد!'
            return render(request, 'home/phone_number_form.html', {'error': message, 'form': form})