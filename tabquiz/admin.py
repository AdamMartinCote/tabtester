from django.contrib import admin

from nested_admin import NestedTabularInline,\
    NestedStackedInline,\
    NestedModelAdmin

from .models import Lesson, Question, Choice


class ChoiceInline(NestedTabularInline):
    fields = [
        'choice_text',
        'next_question'
    ]
    model = Choice
    fk_name = 'level'
    extra = 0


class QuestionInline(NestedStackedInline):
    model = Question
    fk_name = 'level'
    inlines = [ChoiceInline]
    extra = 0


@admin.register(Lesson)
class LessonAdmin(NestedModelAdmin):
    model = Lesson
    inlines = [QuestionInline]
