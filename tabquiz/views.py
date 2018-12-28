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
    return HttpResponse(lesson.description)
    # entry_point = get_object_or_404(Step, lesson_id=lesson_id, start=True)
    # try:
    #     # choices = list(Choice.objects.filter(question=lesson))
    #     entry = 
    # except Choice.DoesNotExist:

    #     raise Http404("no Choices")

    # context = {
    #     'lesson': lesson,
    #     'choices' : choices
    # }
    # return render(request, 'tabquiz/lesson.html', context)
