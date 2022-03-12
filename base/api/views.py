from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Question
from .serailzers import QuestionSerializer


@api_view(['GET'])
def voting_data(request):
    questions = Question.objects.all()
    backend = Question.objects.filter(answer='backend').count()
    frontend = Question.objects.filter(answer='frontend').count()
    fullstack = Question.objects.filter(answer='fullstack').count()
    serializer = QuestionSerializer(questions, many=True)

    data = {
        'backend': backend,
        'frontend': frontend,
        'fullstack': fullstack,
    }

    return Response(serializer.data)
