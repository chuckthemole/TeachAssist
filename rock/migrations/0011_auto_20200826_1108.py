# Generated by Django 3.0.3 on 2020-08-26 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rock', '0010_auto_20200826_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='upload',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rock.Upload'),
        ),
    ]
