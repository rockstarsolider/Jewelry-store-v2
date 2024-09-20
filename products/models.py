from django.db import models
from django.core.validators import FileExtensionValidator
from custom_translate.templatetags.persian_calendar_convertor import format_persian_datetime, convert_to_persian_calendar
from custom_translate.templatetags.custom_translation_tags import translate_number


# Category of product
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=('نام دسته بندی'))
    image = models.ImageField(upload_to='category/', default='/default.png', verbose_name=('تصویر'))
    
    class Meta:
        verbose_name_plural = "دسته بندی ها"
        verbose_name = "دسته بندی"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name=('دسته بندی'))
    name = models.CharField(max_length=75, verbose_name=('نام محصول'))
    description = models.TextField(blank=True, null=True, verbose_name=('توضیحات'))
    price = models.PositiveIntegerField(verbose_name=('قیمت'))
    image = models.ImageField(upload_to='product/', default='/default.png', verbose_name=('تصویر اصلی'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=('منتشر شده در '))
    material = models.CharField(max_length=50, null=True, blank=True, verbose_name=('جنس'))
    weight = models.CharField(max_length=50, null=True, blank=True, verbose_name=('وزن'))
    color = models.CharField(max_length=50, null=True, blank=True, verbose_name=('رنگ'))
    carat = models.CharField(max_length=50, null=True, blank=True, verbose_name=('عیار'))
    
    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"

    @property
    def formatted_created_at(self):
        return translate_number(format_persian_datetime(convert_to_persian_calendar(self.created_at)))
    
    def __str__(self):
        return self.name
    

# Images for products
class Image(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=('نام محصول'))
    image_field = models.ImageField(upload_to='product/', verbose_name=('تصویر'))
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=('بارگذاری شده در '))
    
    class Meta:
        verbose_name_plural = "تصاویر"
        verbose_name = "تصویر"


# Videos for products
class Video(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='videos', verbose_name=('نام محصول'))
    video = models.FileField(upload_to='product/', verbose_name=('ویدیو'), validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=('بارگذاری شده در '))
    
    class Meta:
        verbose_name_plural = "ویدیو ها"
        verbose_name = "ویدیو"