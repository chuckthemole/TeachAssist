# Generated by Django 3.0.3 on 2021-02-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0003_problem_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]