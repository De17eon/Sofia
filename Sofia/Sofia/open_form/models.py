from django.db import models
from authsystem.models import Candidate
from vacancy.models import Vacancy

class OpenForm(models.Model):
    id = models.AutoField(
        primary_key= True
    )

    vacancy_id = models.ForeignKey(
        Vacancy,
        verbose_name='Какой вакансии',
        null= False,
        on_delete = models.CASCADE
    )
    
    order = models.IntegerField(
        verbose_name='Порядковый номер'
    )

    description = models.TextField(
        verbose_name= 'Текст задания'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    

class OpenFormAnswer(models.Model):
    id = models.AutoField(
        primary_key= True
    )
    text = models.TextField(
        verbose_name = 'Ответ на вопрос'
    )
    answer_file = models.FileField(
        upload_to='media/',
        blank= True,
        verbose_name='Прикрепленный файл'
    )
    open_form_id = models.ForeignKey(
        OpenForm,
        null = False,
        on_delete = models.CASCADE
    ) 

    candidate_id = models.ForeignKey(
        Candidate,
        null = False,
        on_delete = models.CASCADE
    )

    mark = models.IntegerField(
        verbose_name= 'Оценка',
        blank = True,
        null = True
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'