# Generated by Django 3.1.6 on 2021-02-19 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0009_quiz_quiz_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]