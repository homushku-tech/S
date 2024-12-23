from main.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('survey', SurveyView)
router.register('questions', QuestionsView)
router.register('answers', AnswersView)
router.register('options', OptionsView)
router.register('responses', ResponsesView)
router.register('answers_selections', AnswerSelectionsView)
router.register('orders', OrderView)
urlpatterns =router.urls