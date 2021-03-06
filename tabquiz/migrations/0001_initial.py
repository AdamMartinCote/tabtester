# Generated by Django 2.1.4 on 2019-01-02 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default=None, upload_to='image/')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabquiz.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabquiz.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='next_question',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_choice', to='tabquiz.Question'),
        ),
    ]
