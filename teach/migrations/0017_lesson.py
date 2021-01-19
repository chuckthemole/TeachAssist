# Generated by Django 3.0.3 on 2021-01-19 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0016_remove_location_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(default='', max_length=30)),
                ('description', models.TextField(default='', max_length=30)),
                ('img', models.ImageField(blank=True, default='static/teach/images/no_image_available.PNG', upload_to='images/')),
                ('img_url', models.TextField(blank=True, default='', max_length=100)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teach.teacher')),
            ],
        ),
    ]
