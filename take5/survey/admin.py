from django.contrib import admin
from .models import *

#pesquisa via admin

class SurveyAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']

class SurveyQuestionAdmin(admin.ModelAdmin):
    search_fields = ['questionID', 'surveyID', 'question_title']

class SurveyQuestionAlternativeAdmin(admin.ModelAdmin):
    search_fields = [ 'surveyID','questionID', 'choice_text']

class SurveyUserAnswerAdmin(admin.ModelAdmin):
    search_fields = [ 'surveyID','questionID', 'user_answerID', 'user','body','choice_text']



admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(SurveyQuestionAlternative, SurveyQuestionAlternativeAdmin)
admin.site.register(SurveyUserAnswer, SurveyUserAnswerAdmin)

