from django.contrib import admin

import nested_admin

from .models import Lesson, Question, Choice


class ChoiceInline(nested_admin.NestedTabularInline):
    fields = [
        'choice_text',
        'next_question'
    ]
    model=Choice
    fk_name= 'level'
    extra=0

class QuestionInline(nested_admin.NestedStackedInline):
    model=Question
    fk_name='level'
    inlines=[ChoiceInline]
    extra=0

class LessonAdmin(nested_admin.NestedModelAdmin):
    model=Lesson
    inlines=[QuestionInline]

admin.site.register(Lesson, LessonAdmin)
# admin.site.register(Question, QuestionAdmin)
