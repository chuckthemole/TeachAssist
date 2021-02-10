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
                    pair = []
                    try:
                        if j == 0:
                            pair.append('A')
                        elif j == 1:
                            pair.append('B')
                        elif j == 2:
                            pair.append('C')
                        else:
                            pair.append('D')
                        answer = request.POST["question" + str(i) + "_answer" + str(j + 1)]
                        pair.append(answer)
                        answers.append(pair)
                    except:
                        Quiz.objects.get(pk=quiz.id).delete()
                        return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson, "error":"Please choose answers for all questoins!"})
                problem = Problem.objects.create(teacher = teacher, quiz = quiz, question = question, answers = answers)
                problem = get_object_or_404(Problem, pk=problem.id)
                problem.save()
                i += 1

def show_quiz(request, quiz_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            quiz = get_object_or_404(Quiz, pk=quiz_id)
            if quiz:
                problems = Problem.objects.filter(quiz=quiz)
                return render(request, "teach/quiz/show_quiz.html", {"user":user, "quiz":quiz, "problems":problems})
        return redirect("teach:login")

def show_all_quizzes(request, lesson_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            quizzes = Quiz.objects.filter(lesson=lesson)
            number_of_quizzes = len(quizzes)
            return render(request, "teach/quiz/show_all_quizzes.html", {"user":user, "lesson":lesson, "quizzes":quizzes, "number_of_quizzes":number_of_quizzes})

def edit_quiz(request):
    pass

def update_quiz(request):
    pass

def delete_quiz(request, quiz_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return HttpResponse(status=500)
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        lesson = get_object_or_404(Lesson, pk=quiz.lesson.id)
        if quiz.teacher.user.id == user.id:
            Quiz.objects.get(pk=quiz_id).delete()
            quizzes = Quiz.objects.filter(lesson=lesson)
            number_of_quizzes = len(quizzes)
            return render(request, "teach/quiz/show_all_quizzes.html", {"user":user, "lesson":lesson, "quizzes":quizzes, "number_of_quizzes":number_of_quizzes})
        quizzes = Quiz.objects.filter(lesson=lesson)
        number_of_quizzes = len(quizzes)
        return render(request, "teach/quiz/show_all_quizzes.html", {"user":user, "lesson":lesson, "quizzes":quizzes, "number_of_quizzes":number_of_quizzes})
    else:
        return HttpResponse(status=500)

def switch_public_private(request):
    pass
