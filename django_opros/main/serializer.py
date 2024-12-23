from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from main.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"

class QuestionsSerializer(ModelSerializer):
    survey = SurveySerializer()
    class Meta:
        model = Questions
        fields = "__all__"

class OptionsSerializer(ModelSerializer):
    question = QuestionsSerializer()
    class Meta:
        model = Options
        fields = "__all__"

class AnswersSerializer(ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"

class ResponsesSerializer(ModelSerializer):
    class Meta:
        model = Responses
        fields = "__all__"

class AnswerSelectionsSerializer(ModelSerializer):
    class Meta:
        model = AnswerSelections
        fields = "__all__"

class OrderSerializer(ModelSerializer):

    class Meta:
        model = News
        fields = ['name', 'text', 'date']

