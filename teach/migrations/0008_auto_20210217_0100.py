# Generated by Django 3.1.6 on 2021-02-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0007_auto_20210214_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='correct_answer',
            field=models.TextField(default='A', max_length=1),
        ),
    ]
