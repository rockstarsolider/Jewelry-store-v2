from django import forms  
from django.core.exceptions import ValidationError  
import re  

class PhoneNumberForm(forms.Form):  
    phone_number = forms.CharField(  
        max_length=14,   
        required=True,   
        widget=forms.TextInput(attrs={  
            'class': 'input input-bordered',   
            'placeholder': 'شماره خود را وارد کنید'  
        }) 
    )  

    def clean_phone_number(self):  
        phone_number = self.cleaned_data.get('phone_number')  

        # Example of basic validation (check if it only contains digits)  
        if not re.match(r'^[0-9]+$', phone_number):  
            raise ValidationError('شماره تلفن باید فقط عدد باشد')  

        # Additional validation (e.g., length check)  
        if len(phone_number) < 10:  
            raise ValidationError('شماره تلفن باید بیشتر از 10 رقم باشد')  
        if len(phone_number) > 13:  
            raise ValidationError('شماره تلفن باید کمتر از 13 رقم باشد')  

        return phone_number 