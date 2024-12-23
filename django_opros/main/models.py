from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    text = models.TextField(blank=True, null=True, verbose_name='Описание')
    date = models.DateField(blank=True, null=True, verbose_name='Дата')

    class Meta:
        db_table = 'news'
        verbose_name = 'Новости'
        ordering = ("id",)

    def __str__(self):
        return self.name

class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    class Meta:
        verbose_name = "Опрос"

    def __str__(self):
        return self.name

class Questions(models.Model):
    TYPES = [
        ('1', 'Одним вариантом'),
        ('2', 'Множественым вариантом ответа'),
        ('3', 'Открытый вопрос'),
    ]
    text = models.CharField(max_length=255)
    type = models.CharField(choices=TYPES, default='1', max_length=1)
    survey = models.ForeignKey(Survey, related_name="questions", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Вопросы"
    def __str__(self):
        return f"{self.survey.name}: {self.text}"

class Options(models.Model):
    question = models.ForeignKey(Questions, related_name="options", on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    def __str__(self):
        return '{}'.format(self.text)

class Responses(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, related_name="responses", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Ответ на  от {self.user}"
class Answers(models.Model):
    responses = models.ForeignKey(Responses, related_name="answers", on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Questions, related_name="answers",  on_delete=models.CASCADE, null=True, blank=True)
    option = models.ForeignKey(Options, related_name="answers", blank=True, null=True, on_delete=models.CASCADE,
                               verbose_name="Выбранный вариант")
    text = models.TextField(blank=True, null=True, verbose_name="Ответ (для открытых вопросов)")
    def __str__(self):
        return f"Ответ на {self.question}"

class AnswerSelections(models.Model):
    answer = models.ForeignKey(Answers, related_name="selections", on_delete=models.CASCADE, verbose_name="Ответ")
    option = models.ForeignKey(Options, related_name="selections", on_delete=models.CASCADE,
                               verbose_name="Выбранный вариант")

    def __str__(self):
        return f"Выбор: {self.option.text}"