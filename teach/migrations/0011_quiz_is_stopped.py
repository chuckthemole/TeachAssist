# Generated by Django 3.1.6 on 2021-02-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0010_quiz_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_stopped',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]