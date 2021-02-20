from django.urls import path, include
from teach.views import quiz
app_name = 'teach'

urlpatterns = [
    # quiz
    path('quiz/<int:lesson_id>/publish', quiz.publish_quiz, name='publish_quiz'),
    path('quiz/<int:lesson_id>/create', quiz.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/show', quiz.show_quiz, name='show_quiz'),
    path('quiz/<int:lesson_id>/show_all_quizzes', quiz.show_all_quizzes, name='show_all_quizzes'),
    path('quiz/show_active_quizzes', quiz.show_active_quizzes, name='show_active_quizzes'),
    path('quiz/<int:quiz_id>/edit', quiz.edit_quiz, name='edit_quiz'),
    path('quiz/<int:quiz_id>/update', quiz.update_quiz, name='update_quiz'),
    path('quiz/<int:quiz_id>/delete', quiz.delete_quiz, name='delete_quiz'),
    path('quiz/<int:problem_id>/delete_problem', quiz.delete_problem, name='delete_problem'),
    path('quiz/<int:quiz_id>/take_quiz', quiz.take_quiz, name='take_quiz'),
    path('quiz/<int:quiz_id>/teacher_submit_quiz', quiz.teacher_submit_quiz, name='teacher_submit_quiz'),
    path('quiz/<int:student_id>/submit_quiz', quiz.submit_quiz, name='submit_quiz'),
    path('quiz/<int:quiz_id>/switch', quiz.switch_public_private, name='switch_public_private'),
    path('quiz/find_quiz', quiz.find_quiz, name='find_quiz'),
    path('quiz/<int:quiz_id>/create_quiz_code', quiz.create_quiz_code, name='create_quiz_code'),
    path('quiz/<int:quiz_id>/restart_quiz', quiz.restart_quiz, name='restart_quiz'),
    path('quiz/<int:quiz_id>/stop_quiz', quiz.stop_quiz, name='stop_quiz'),
    path('quiz/<int:quiz_id>/show_quiz_results', quiz.show_quiz_results, name='show_quiz_results'),
]
