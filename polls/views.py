from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    choice = get_object_or_404(Choice, pk=question_id)
    return render(request, 'polls/results.html', {'choice' : choice})

def vote(request, question_id):
    vote = get_object_or_404(Choice.votes)
    return render(request, 'polls/vote.html', {'vote' : vote} )