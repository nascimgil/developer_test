from rest_framework import serializers
from survey.models import *

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'

class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = '__all__'

class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = '__all__'

class SurveyUserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyUserAnswer
        fields = '__all__'