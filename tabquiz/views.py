from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Lesson, Question, Choice


class LessonIndexView(ListView):
    model = Lesson
    template_name='tabquiz/index.html'
    context_object_name='lesson_list'

def lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    if request.method == 'GET':
        # FIXME: should not be hardcoded to question[0]
        question = lesson.question_set.all()[0]
        route = list()

    elif request.method == 'POST':
        choice = Choice.objects.get(pk=request.POST['choice'])
        question = choice.next_question
        route = request.session['route']
        route.append(question.pk)

    request.session['route'] = route
    context = {
        'lesson': lesson,
        'lesson_list': Lesson.objects.all(),
        'question': question,
        'choices': question.choice_set.all(),
        'route': route,
    }
    return render(request, 'tabquiz/lesson.html', context)
