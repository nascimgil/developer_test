from rest_framework.response import Response
from rest_framework.decorators import api_view
from survey.models import *
from .serializers import *

### Get Views
@api_view(['GET'])
def getSurvey(request):
    data = Survey.objects.all()
    serializer = SurveySerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSurveyQuestion(request):
    data = SurveyQuestion.objects.all()
    serializer = SurveySerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSurveyQuestionAlternative(request):
    data = SurveyQuestionAlternative.objects.all()
    serializer = SurveySerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSurveyUserAnswer(request):
    data = SurveyUserAnswer.objects.all()
    serializer = SurveySerializer(data, many=True)
    return Response(serializer.data)



### Post Views
@api_view(['POST'])
def addSurvey(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addSurveyQuestion(request):
    serializer = SurveyQuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addSurveyQuestionAlternative(request):
    serializer = SurveyQuestionAlternativeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addSurveyUserAnswer(request):
    serializer = SurveyUserAnswer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)