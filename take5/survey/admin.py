from django.contrib import admin
from .models import *

admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionAlternative)
admin.site.register(SurveyUserAnswer)
