from django.contrib import admin
from .models import *
admin.site.register(Survey)
admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(Answers)
admin.site.register(Responses)
admin.site.register(AnswerSelections)
admin.site.register(News)