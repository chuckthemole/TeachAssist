from django.urls import path, include
from teach.views import lesson
app_name = 'teach'

urlpatterns = [
    # Lesson
    path('lesson/publish', lesson.publish_lesson, name='publish_lesson'),
    path('lesson/create', lesson.create_lesson, name='create_lesson'),
    path('lesson/<int:lesson_id>/show', lesson.show_lesson, name='show_lesson'),
    path('lesson/<int:lesson_id>/edit', lesson.edit_lesson, name='edit_lesson'),
    path('lesson/<int:lesson_id>/update', lesson.update_lesson, name='update_lesson'),
    path('lesson/<int:lesson_id>/delete', lesson.delete_lesson, name='delete_lesson'),
    path('image/<int:lesson_id>/publish', lesson.publish_image, name='publish_image'),
    path('image/<int:lesson_id>/create', lesson.create_image, name='create_image'),
    path('image/<int:lesson_id>/show', lesson.show_image, name='show_image'),
    path('lesson/<int:lesson_id>/switch', lesson.switch_public_private, name='switch_public_private'),
]
