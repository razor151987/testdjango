from django.shortcuts import render
from .models import Question

def index(request):
    question = Question.objects.first()
    return render(request, 'polls/index.html', {'question': question})