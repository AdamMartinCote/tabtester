from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question, Choice


def index(request):
    return HttpResponse("hello")

def lesson(request, lesson_id):
    question = get_object_or_404(Question, lesson_id=lesson_id, question_id=1)
    try:
        choices = list(Choice.objects.filter(question=question))
    except Choice.DoesNotExist:
        raise Http404("no Choices")

    context = {
        'question': question,
        'choices' : choices
    }
    return render(request, 'tabquiz/lesson.html', context)
    # return HttpResponse("this is lesson\n%s" % question.question_text)

