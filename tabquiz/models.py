from django.db import models


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)

    text = models.CharField(max_length=200)

    image = models.ImageField(
            upload_to='image/',
            default=None,
            blank=True)

    def __str__(self):
        return self.text


class Lesson(models.Model):
    lesson_id = models.IntegerField(primary_key=True)
    starting_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    
class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choice_set',
        default=""
    )

    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
