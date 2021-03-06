# Generated by Django 3.0.3 on 2021-01-27 01:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('img', models.ImageField(blank=True, default='static/teach/images/no_image_available.PNG', upload_to='images/teachers')),
                ('is_teacher', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=30)),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('feedback', models.TextField(blank=True, max_length=200)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teach.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(default='', max_length=30)),
                ('subject_class', models.TextField(default='', max_length=30)),
                ('topic', models.TextField(default='', max_length=30)),
                ('lesson_name', models.TextField(default='', max_length=30)),
                ('description', models.TextField(default='', max_length=100)),
                ('img', models.ImageField(blank=True, default='static/teach/images/no_image_available.PNG', upload_to='images/lessons')),
                ('img_url', models.TextField(blank=True, default='', max_length=100)),
                ('icon', models.TextField(default='https://img.icons8.com/dusk/50/000000/book-and-pencil.png', max_length=200)),
                ('is_public', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teach.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=100)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teach.Review')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teach.teacher')),
            ],
        ),
    ]
