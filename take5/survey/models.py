from django.db import models

from django.db import models
from django.contrib.auth.models import User

#Survey (Pesquisa)
#SurveyQuestion (Perguntas da pesquisa)
#SurveyQuestionAlternative (Alternativas para as perguntas da pesquisa)
#SurveyUserAnswer (Respostas dos usuários para a Pesquisa)

class Survey(models.Model):
    surveyID = models.BigAutoField(primary_key=True)  #PK
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=512, blank=True)

class SurveyQuestion(models.Model):
    questionID = models.BigAutoField(primary_key=True) #PK
    surveyID = models.ForeignKey(Survey, null=True, on_delete=models.CASCADE) #related_name="survey",   #FK
    question_title = models.CharField(max_length=255)

class SurveyQuestionAlternative(models.Model):
    surveyID = models.ForeignKey(Survey, null=True, on_delete=models.CASCADE) #FK
    questionID = models.ForeignKey(Survey, related_name='SurveyQuestionAlternative-questionID+', null=True, on_delete=models.CASCADE) #FK     
    question_alternativeID = models.BigAutoField(primary_key=True) #PK
    choice_text = models.CharField(max_length=200)

class SurveyUserAnswer(models.Model):
    surveyID = models.ForeignKey(Survey, null=True, on_delete=models.CASCADE)#FK
    questionID = models.ForeignKey(Survey, related_name='SurveyQuestionAlternative-questionID+', null=True,  on_delete=models.CASCADE)#FK    
    user_answerID = models.ForeignKey(SurveyQuestionAlternative, null=True, on_delete=models.CASCADE) #PK
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #FK
    body = models.CharField(max_length=512)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
