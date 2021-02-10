from .imports import *

def publish_quiz(request, lesson_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson})

def create_quiz(request, lesson_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")

        teacher = user.teacher
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        name = request.POST["name"]
        if not name:
            return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson, "error":"Please choose a name for your lesson!"})

        try:
            quiz = Quiz.objects.create(teacher = teacher, lesson = lesson, name = name)
            quiz = get_object_or_404(Quiz, pk=quiz.id)
            quiz.save()
        except:
            return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson, "error":"Can't create your quiz!"})

        i = 1
        while True:
            try:
                question = request.POST["question" + str(i)]
            except:
                question = None
            if not question and i == 1:
                Quiz.objects.get(pk=quiz.id).delete()
                return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson, "error":"Please choose questions for your lesson!"})
            elif not question:
                problems = Problem.objects.filter(quiz=quiz)
                return render(request, "teach/quiz/show_quiz.html", {"user":user, "quiz":quiz, "problems":problems})
            else:
                answers = []
                for j in range(4):
                    try:
                        answer = request.POST["question" + str(i) + "_answer" + str(j + 1)]
                        answers.append(answer)
                    except:
                        Quiz.objects.get(pk=quiz.id).delete()
                        return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson, "error":"Please choose answers for all questoins!"})
                problem = Problem.objects.create(teacher = teacher, quiz = quiz, question = question, answers = answers)
                problem = get_object_or_404(Problem, pk=quiz.id)
                problem.save()
                i += 1

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
