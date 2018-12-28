from django.contrib import admin

from .models import Lesson, Question, Choice

class LessonAdmin(admin.ModelAdmin):
    pass

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=0

class QuestionAdmin(admin.ModelAdmin):
    inlines=[ChoiceInline]
    
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)

