# Generated by Django 2.0 on 2018-12-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabquiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lesson_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]