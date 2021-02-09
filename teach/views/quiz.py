from .imports import *

def publish_quiz(request, lesson_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            form = Lesson_Form()
            return render(request, "teach/quiz/create_quiz.html", {"user":user, "form":form})

def create_quiz(request):
    pass

def show_quiz(request, lesson_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            if lesson.teacher.id != user.teacher.id:
                if not lesson.is_public:
                    all_lessons = Lesson.objects.all()
                    return render(request, "teach/index.html", {"user":user, "all_lessons": all_lessons})
            return render(request, "teach/lesson/show_lesson.html", {"user":user, "lesson":lesson})

def show_all_quizzes(request, lesson_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            return render(request, "teach/quiz/show_all_quizzes.html", {"user":user})

def edit_quiz(request):
    pass

def update_quiz(request):
    pass

def delete_quiz(request):
    pass

def switch_public_private(request):
    pass
