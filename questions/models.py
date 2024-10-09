from django.db import models

# Create your models here.
class Question(models.Model):
    phone_number = models.CharField(max_length=15, verbose_name='شماره تلفن')
    question_text = models.TextField(verbose_name='شماره تلفن')
    date = models.DateField(auto_now_add=True, verbose_name='شماره تلفن')
    answered = models.BooleanField(default=False, verbose_name='جواب داده شده')

    class Meta:
        verbose_name_plural = "پرسش ها"
        verbose_name = "پرسش"