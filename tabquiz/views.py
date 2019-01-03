from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView

import pdb

from .models import Lesson, Question, Choice

class LessonIndexView(ListView):
    model = Lesson
    template_name='tabquiz/index.html'
    context_object_name='lesson_list'

def lesson(request, lesson_id):
    msg = False
    lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    if request.method == 'GET':
        # FIXME: should not be hardcoded to question[0]
        question = lesson.question_set.all()[0]
        request.session['route'] = list()

    elif request.method == 'POST':
        choice_number = request.POST['choice']
        choice = Choice.objects.get(pk=choice_number)
        question = choice.next_question
        route_list = request.session['route']
        route_list.append(question.pk)
        request.session['route'] = route_list
        print(request.session['route'])
        # import pdb; pdb.set_trace()

    choices = question.choice_set.all()
    lesson_list = Lesson.objects.all()
    context = {
        'lesson': lesson,
        'lesson_list': lesson_list,
        'question': question,
        'choices': choices,
    }
    return render(request, 'tabquiz/lesson.html', context)
