from django.contrib import admin
from .models import teacher, Lesson, Review, Comment, Quiz, Problem, Student, Submitted_Problem

admin.site.register(teacher)
admin.site.register(Lesson)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Quiz)
admin.site.register(Problem)
admin.site.register(Student)
admin.site.register(Submitted_Problem)
