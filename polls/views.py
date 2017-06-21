# from django.shortcuts import render


from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from mysite import settings

from .models import Question, Choice

# from django.template import loader

def get_image_root():
    return ("/polls" + settings.MEDIA_URL)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now())[:5]
        # return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'



def hints(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(str(question))
    all_hints = question.images.all()
    return render(request, 'polls/hints.html', {'question': question, 'hints': all_hints, 'image_root': get_image_root()})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # first_question = Question.objects.get(pk=1)
        choice_index = request.POST['choice']
        choice_set = question.choice_set
        selected_choice = choice_set.get(pk=choice_index)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# deprecated by DetailView
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# deprecated by ResultsView
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})



# deprecated by IndexView
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:3]
#     # template = loader.get_template('polls/index.html')
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
