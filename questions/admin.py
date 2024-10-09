from django.contrib import admin
from .models import Question
from custom_translate.templatetags.persian_calendar_convertor import convert_to_persian_calendar_date, format_persian_date

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'formatted_date', 'answered']
    list_filter = ['date', 'answered']
    search_fields = ['phone_number', 'question_text']
    list_editable = ['answered']

    def formatted_date(self, obj):
        return format_persian_date(convert_to_persian_calendar_date(obj.date))


admin.site.register(Question, QuestionAdmin)