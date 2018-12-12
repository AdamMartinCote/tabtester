from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_id = models.IntegerField(
            primary_key=True)
    lesson_id = models.IntegerField()
    image = models.ImageField(
            upload_to='image/',
            default=None,
            blank=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE,
            related_name='choice_question',
            default="")
    choice_text = models.CharField(max_length=200)
    # next_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice_target', null=True)

    def __str__(self):
        return self.choice_text

