from django import forms  
from .models import Question

class QuestionForm(forms.ModelForm):  
    class Meta:  
        model = Question  
        fields = ['phone_number', 'question_text',]  
        widgets = {  
            'phone_number': forms.TextInput(attrs={'placeholder': 'شماره تلفن ...'}),  
            'question_text': forms.Textarea(attrs={'placeholder': 'سوال ...', 'rows': 4}),  
        }  

    def clean_phone_number(self):  
        phone_number = self.cleaned_data.get('phone_number')  
        if not phone_number.isdigit():  
            raise forms.ValidationError("برای شماره تلفن فقط عدد وارد کنید")  
        if len(phone_number) <= 10 or len(phone_number) > 13:  
            raise forms.ValidationError("شماره تلفن باید بین 11 تا 13 رقم باشد")  
        return phone_number  

    def clean_question_text(self):
        question_text = self.cleaned_data.get('question_text')
        if not question_text:
            raise forms.ValidationError("سوال خود را بنویسید")  
        return question_text