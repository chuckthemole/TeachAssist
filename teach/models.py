import os
import uuid

from django.db import models
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

class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

class Lesson(models.Model):
	def __str__(self):
		return (self.subject + " \n" + self.lesson_name)

	# FK
	teacher = models.ForeignKey(teacher, on_delete=models.CASCADE, null=True)

	subject = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	subject_class = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	topic = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	lesson_name = models.TextField(max_length=30, null=False, blank=False, unique=False, default="")
	description = models.TextField(max_length=100, null=False, blank=False, unique=False, default="")

	# Image of location
	img = models.ImageField(upload_to='images/', blank=True, default="static/teach/images/no_image_available.PNG")
	img_url = models.TextField(max_length=100, null=False, blank=True, unique=False, default="")
	icon = models.TextField(max_length = 200, default="https://img.icons8.com/dusk/50/000000/book-and-pencil.png")

	is_public = models.BooleanField(default=True)

	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now=True)

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
