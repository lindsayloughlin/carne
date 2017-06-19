# from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from django.shortcuts import get_list_or_404, render, get_object_or_404


# from django.template import loader


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're look at question %s" % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # response = "You're looking at the results of question %s"
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question, id)))
        # return HttpResponse("You're voting on question %s" % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    # template = loader.get_template('polls/index.html')
    # output = ', '.join([q.question_text for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index. 123565")
