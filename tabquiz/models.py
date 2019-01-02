from django.db import models


class Lesson(models.Model):
    lesson_id = models.IntegerField(primary_key=True)

    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Question(models.Model):
    level = models.ForeignKey('Lesson', on_delete=models.CASCADE,)

    question_id = models.AutoField(primary_key=True)

    text = models.CharField(max_length=200)

    # lesson = models.ForeignKey(
    #     Lesson,
    #     on_delete=models.CASCADE,
    #     unique=True,
    #     default="",
    # )

    image = models.ImageField(
            upload_to='image/',
            default=None,
            blank=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    level = models.ForeignKey('Question', on_delete=models.CASCADE,)

    # question = models.ForeignKey(
    #     Question,
    #     on_delete=models.CASCADE,
    #     related_name='choice_set',
    #     default=""
    # )
    next_question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='parent_choice',
        default="",
        null=True,
        blank=True,
    )

    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
