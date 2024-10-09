from django.shortcuts import render  
from .forms import QuestionForm
from django.views import View

class QuestionView(View):  
    def get(self, request):
        form = QuestionForm()
        return render(request, 'question_form.html', {'form': form})  

    def post(self, request):  
        form = QuestionForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return render(request, 'question_form.html', {'form': QuestionForm(), 'success': True})  
        
        return render(request, 'question_form.html', {'form': form})