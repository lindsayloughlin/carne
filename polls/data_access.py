from django.core import serializers
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from polls.models import Question


def question_json(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # django doesn't like putting things in a map.
    data = serializers.serialize('json', [ question, ])
    return HttpResponse(data)