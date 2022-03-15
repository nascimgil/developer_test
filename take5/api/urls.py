from django.urls import path
from . import views

urlpatterns = [ 
    path('survey',views.getSurvey),
    path('survey-question', views.getSurveyQuestion),
    path('question-alternative', views.getSurveyQuestion),
    path('user-answer', views.getSurveyUserAnswer),

    path('add-survey', views.addSurvey),
    path('add-survey-question', views.addSurveyQuestion),
    path('add-question-alternative', views.addSurveyQuestionAlternative),
    path('add-user-answer', views.addSurveyUserAnswer),
]