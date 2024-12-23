from django.shortcuts import render
from django.contrib import messages

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import generics

from rest_framework.filters import SearchFilter
from main.models import *
from rest_framework.viewsets import ModelViewSet
from main.serializer import *

from django_filters.rest_framework import DjangoFilterBackend

import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .tasks import fetch_news

def index(request):
    fetch_news.delay()  # Запускаем задачу в фоновом режиме
    return HttpResponse("hello world11")

class SurveyView(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    filter_backends = [SearchFilter,]
    search_fields = ["name"]

class QuestionsView(ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class OptionsView(ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class AnswersView(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['responses']

class ResponsesView(ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['survey']

class AnswerSelectionsView(ModelViewSet):
    queryset = AnswerSelections.objects.all()
    serializer_class = AnswerSelectionsSerializer

class OrderView(ModelViewSet):

    def get():
        url = 'https://rtyva.ru/'
        page = requests.get(url).text
        soup = BeautifulSoup(page)
        news_items = soup.find_all(class_='news-item')

        for item in news_items[1:10]:
            news_name = item.find(class_='news-name').find('b').get_text()
            news_text = item.find(class_='news-text').find(class_='news-preview-text').find('p').get_text()
            try:
                News.objects.create(name=news_name, text=news_text)
            except:
                continue
    get()

    queryset = News.objects.all()
    serializer_class = OrderSerializer

