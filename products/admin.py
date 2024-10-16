from django.contrib import admin
from .models import Category, Product, Image, Video, PhoneNumber
from custom_translate.templatetags.persian_calendar_convertor import convert_to_persian_calendar ,format_persian_datetime
from custom_translate.templatetags.custom_translation_tags import translate_number
from import_export.admin import ImportExportModelAdmin
from .resource import ProductResource
from django.db import models
from django import forms
from django.contrib.auth.models import User, Group
from admin_interface.models import Theme
from django.utils.html import format_html

# This function translates numbers to persian. e.g. 25 => ۲۵
def fa_num(num):
    return translate_number(f'{num:,}')


class ProductAdmin(ImportExportModelAdmin):
    search_fields = ("name", 'id', 'description', 'price', 'created_at')
    list_display = ('image_tag', 'pid', 'name', 'formatted_price', 'category_id', 'formatted_created_at')
    list_display_links = ('pid', 'name',)
    list_filter = ('category_id', 'created_at')
    actions = ('delete_image', 'set_price_to_zero',)
    resource_class = ProductResource # Recource model for django import-export

    def delete_image(self, request, queryset):
        queryset.update(image='/default.png')
        self.message_user(request, "تصاویر محصولات انتخاب شده حذف شدند")
    delete_image.short_description = "حذف تصویر محصولات انتخاب شده"

    def set_price_to_zero(self, request, queryset): # All selected products price will be set to zero
        queryset.update(price=0)
        self.message_user(request, "قیمت محصولات انتخاب شده صفر شدند")
    set_price_to_zero.short_description = "صفر کردن قیمت محصولات انتخاب شده"

    def formatted_created_at(self, obj):  
        return obj.formatted_created_at  
    formatted_created_at.short_description = 'تاریخ'  # Set the column header  
    formatted_created_at.admin_order_field = 'created_at'  # Specify the field to order by
    
    def pid(self, obj):
        return fa_num(obj.id)
    pid.short_description = 'id'

    def formatted_price(self, obj):   
        return f"{fa_num(obj.price)} تومان "
    formatted_price.short_description = 'قیمت'
    formatted_price.admin_order_field = 'price'

    formfield_overrides = {
        models.IntegerField: {'widget': forms.NumberInput(attrs={'size': '50'})},
        models.TextField: {"widget": forms.Textarea()},
    }

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width: 32px; height:32px;" />'.format(obj.image.url))
    image_tag.short_description = 'تصویر'


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ('name','image_tag',)
    actions = ('delete_image',)

    def delete_image(self, request, queryset):
        queryset.update(image='/default.png')
        self.message_user(request, "تصاویر دسته بندی های انتخاب شده حذف شدند")
    delete_image.short_description = "حذف تصویر دسته بندی های انتخاب شده"

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width: 32px; height:32px" />'.format(obj.image.url))
    image_tag.short_description = 'تصویر'


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag','product_id', 'datetime')
    search_fields = ("product_id",'image_field')
    list_filter = ('uploaded_at','product_id')
    list_display_links = ('product_id', 'image_tag')

    def datetime(self, obj):
        return translate_number(format_persian_datetime(convert_to_persian_calendar(obj.uploaded_at)))
    datetime.short_description = 'آپلود شده در'

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width: 32px; height:32px;" />'.format(obj.image_field.url))
    image_tag.short_description = 'تصویر'


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_tag','product_id', 'datetime')
    search_fields = ("product_id",'video')
    list_filter = ('uploaded_at','product_id')
    list_display_links = ('product_id', 'video_tag')

    def datetime(self, obj):
        return translate_number(format_persian_datetime(convert_to_persian_calendar(obj.uploaded_at)))
    datetime.short_description = 'آپلود شده در'

    def video_tag(self,obj):
        return format_html('<video src="{0}" style="width: 32px; height:32px;" />'.format(obj.video.url))
    video_tag.short_description = 'تصویر'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(PhoneNumber)