# Generated by Django 3.0.3 on 2021-01-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0020_auto_20210122_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
