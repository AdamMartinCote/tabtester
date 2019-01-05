from django.db import models
from django.utils.translation import gettext_lazy as _


class Lesson(models.Model):
    lesson_id = models.IntegerField(
        primary_key=True,
        verbose_name=_('lesson id'),
    )

    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')


class Question(models.Model):
    level = models.ForeignKey('Lesson', on_delete=models.CASCADE,)

    question_id = models.AutoField(primary_key=True)

    text = models.CharField(
        max_length=200,
        verbose_name=_('text'),
    )

    image = models.ImageField(
        upload_to='image/',
        default=None,
        blank=True)

    is_final = models.BooleanField(
        default=False,
        # Translators: indicates the final question of a lesson
        verbose_name=_('final question')
    )

    def __str__(self):
        return self.text


class Choice(models.Model):
    level = models.ForeignKey('Question', on_delete=models.CASCADE,)

    next_question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='parent_choice',
        default='',
        null=True,
        blank=True,
        verbose_name=_("next question"),
    )

    choice_text = models.CharField(
        max_length=200,
        verbose_name=_('choice text'),
    )

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = _('Choices')
        verbose_name_plural = _('Choices')
