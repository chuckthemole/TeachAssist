# Generated by Django 3.0.3 on 2020-08-26 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0009_auto_20200826_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='upload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rock.Upload'),
        ),
    ]
