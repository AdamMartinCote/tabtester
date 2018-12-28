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
        question = lesson.starting_question
        choices = question.choice_set.all()

    elif request.method == 'POST':
        question = Question.objects.get(pk=1) # MOCK
        choices = question.choice_set.all()
        
    context = {
        'lesson': lesson,
        'question': question,
        'choices': choices,
    }
    return render(request, 'tabquiz/lesson.html', context)
