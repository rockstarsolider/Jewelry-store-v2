from django.shortcuts import render, get_object_or_404  
from django.views import View
from .models import Product, Category, Image, Video
from django.db import models
from .forms import PhoneNumberForm  
from .models import PhoneNumber
from django.http import JsonResponse

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
    

class ProductsView(View):   # Products page
    def get(self, request):
        selected_category = request.GET.get('category')
        order = request.GET.get('order', '-created_at')  # Default to 'latest' if not specified
        products = Product.objects.all().order_by(order)
        categories = Category.objects.all()[:20]
        if selected_category:  
            products = products.filter(category_id__name=selected_category)
        context = {
            'form': PhoneNumberForm(),
            'products': products,
            'categories': categories,
            'selected_category': selected_category or '',
            'order': order
        }
        return render(request, 'products/products.html', context)
    

class AboutUsView(View):
    def get(self, request):
        return render(request, 'products/about_us.html')
    

# Detail of a product
class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        images = Image.objects.filter(product_id=product)
        videos = Video.objects.filter(product_id=product)
        related_products = Product.objects.filter(category_id = product.category_id).order_by('-created_at')[:20]
        context = {
            'product': product,
            'products': related_products,
            'form': PhoneNumberForm(),
            'images': images,
            'videos': videos
        }
        return render(request, 'products/product.html', context)


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


class SearchProducts(View):
    def get(self, request, search_text):
        search = Product.objects.filter(name__contains=search_text)
        return render(request, 'partial/search_comp.html', {'search':search})