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
            raise ValidationError('Phone number must contain only digits.')  

        # Additional validation (e.g., length check)  
        if len(phone_number) < 10:  
            raise ValidationError('Phone number must be at least 10 digits long.')  

        return phone_number 