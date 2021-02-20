import os
import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

class teacher(models.Model):
	def __str__(self):
		return self.user.username

	#teacher_yet = models.BooleanField(default=False)  # the user is not a coder yet
	#local = models.BooleanField(default=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created = models.DateField(auto_now=True)   # maybe redundant, user model has date_joined :)
	updated = models.DateField(auto_now=True)
	img = models.ImageField(upload_to='images/teachers', blank=True, default="static/teach/images/no_image_available.PNG")
	is_teacher = models.BooleanField(default=True)

class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

class Lesson(models.Model):
	def __str__(self):
		return ("Subject: " + self.subject + " \n" + "Title: " + self.lesson_name)

	# FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)

	subject = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	subject_class = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	topic = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	lesson_name = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	description = models.TextField(max_length=300, null=False, blank=False, unique=False, default="")
	instructions = models.TextField(max_length=300, null=True, blank=True, unique=False, default="")
	game_link = models.URLField(max_length = 200, null=True, blank=True, unique=False, default="")

	# Image of location
	img = models.ImageField(upload_to='images/lessons', blank=True, default="static/teach/images/no_image_available.PNG")
	img_url = models.TextField(max_length=100, null=False, blank=True, unique=False, default="")
	icon = models.TextField(max_length = 200, default="https://img.icons8.com/dusk/50/000000/book-and-pencil.png")

	is_public = models.BooleanField(default=True)
	number_of_quizzes = models.IntegerField(blank=False, default=0)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

class Quiz(models.Model):
	# FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)

	name = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	number_of_problems = models.IntegerField(blank=False, default=0)
	quiz_code = models.TextField(max_length=6, null=True, blank=True, unique=True, default="")
	is_active = models.BooleanField(null=True, blank=True, default=False, unique=False)
	is_stopped = models.BooleanField(null=True, blank=True, default=True, unique=False)
	created = models.DateField(auto_now=True)

class Problem(models.Model):
	# FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)

	question = models.TextField(max_length=100, null=False, blank=False, unique=False, default="")
	answers = ArrayField(ArrayField(models.TextField(max_length=30, null=False, blank=False, unique=False, default=""), size=2,), 4,)
	correct_answer = models.TextField(max_length=1, null=False, blank=False, unique=False, default="A")

class Student(models.Model):
	# FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)

	name = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")

class Submitted_Problem(models.Model):
	# FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
	problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)

	submitted_answer = models.TextField(max_length=1, null=False, blank=False, unique=False, default="")

class Review(models.Model):
	def __str__(self):
		return self.title

	#FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)

	title = models.TextField(max_length=30, null=False, blank=False, unique=False)
	stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	feedback = models.TextField(max_length=200, unique=False, blank=True)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

	#class Meta:
		#unique_together = (('teacher', 'destination'),)

class Comment(models.Model):
	def __str__(self):
		return self.body
	# FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)
	review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)

	body = models.TextField(max_length=100, null=False, blank=False, unique=False)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

@receiver(models.signals.post_delete, sender=Lesson)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)

@receiver(models.signals.pre_save, sender=Lesson)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Lesson.objects.get(pk=instance.pk).img
    except Lesson.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

@receiver(models.signals.post_delete, sender=teacher)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)

@receiver(models.signals.pre_save, sender=teacher)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = teacher.objects.get(pk=instance.pk).img
    except Lesson.DoesNotExist:
        return False

    new_file = instance.img
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
