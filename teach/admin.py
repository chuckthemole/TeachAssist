from django.contrib import admin
from .models import teacher, Lesson, Review, Comment

admin.site.register(teacher)
admin.site.register(Lesson)
admin.site.register(Review)
admin.site.register(Comment)
