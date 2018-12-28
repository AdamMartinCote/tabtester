from django.urls import path

from . import views
from tabquiz.views import LessonIndexView

app_name='tabquiz'
urlpatterns = [
    path('', LessonIndexView.as_view(), name='index'),
    path('lesson/<int:lesson_id>/', views.lesson, name='lesson'),
]

