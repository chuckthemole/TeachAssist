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
            return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson, "error":"Please choose a name for your quiz!"})

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
                return render(request, "teach/quiz/create_quiz.html", {"user":user, "lesson":lesson, "error":"Please create questions!"})
            elif not question:
                p = Problem.objects.filter(quiz=quiz)
                problems = []
                for i in range(len(p)):
                    item = []
                    item.append(i + 1)
                    item.append(p[i])
                    problems.append(item)
                quizzes = Quiz.objects.filter(lesson=lesson)
                number_of_quizzes = len(quizzes)
                lesson.number_of_quizzes = number_of_quizzes
                lesson.save()
                number_of_problems = len(p)
                quiz.number_of_problems = number_of_problems
                quiz.save()
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
                correct_answer = request.POST["correct_answer" + str(i)]
                problem = Problem.objects.create(teacher = teacher, quiz = quiz, question = question, answers = answers, correct_answer=correct_answer)
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
                p = Problem.objects.filter(quiz=quiz)
                problems = []
                for i in range(len(p)):
                    item = []
                    item.append(i + 1)
                    item.append(p[i])
                    problems.append(item)
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
            number_of_quizzes = lesson.number_of_quizzes
            return render(request, "teach/quiz/show_all_quizzes.html", {"user":user, "lesson":lesson, "quizzes":quizzes, "number_of_quizzes":number_of_quizzes})

def show_quiz_with_numbered_problems(request, quiz):
    user = quiz.teacher.user
    p = Problem.objects.filter(quiz=quiz)
    problems = []
    for i in range(len(p)):
        item = []
        item.append(i + 1)
        item.append(p[i])
        problems.append(item)
    return render(request, "teach/quiz/show_quiz.html", {"user":user, "quiz":quiz, "problems":problems})

def edit_quiz(request, quiz_id):
    if request.method == "GET":
         user = request.user
         if not user.is_authenticated:
             return redirect("collections:login")

         quiz = get_object_or_404(Quiz, pk=quiz_id)

         if quiz.teacher.user.id == request.user.id:
             lesson = get_object_or_404(Lesson, pk=quiz.lesson.id)
             p = Problem.objects.filter(quiz=quiz)
             problems = [] # Problems with numbers attached
             for i in range(len(p)):
                 item = []
                 item.append(i + 1)
                 item.append(p[i])
                 problems.append(item)
             return render(request, "teach/quiz/edit_quiz.html", {"user":user, "lesson":lesson, "quiz":quiz, "problems":problems})
         else:
             return render(request, "teach/index.html",
             {"error":"You are not the author of the quiz that you tried to edit."})

def update_quiz(request, quiz_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        teacher = user.teacher
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        name = request.POST["name"]
        lesson = get_object_or_404(Lesson, pk=quiz.lesson.id)
        p = Problem.objects.filter(quiz=quiz)
        problems = [] # Problems with numbers attached
        for i in range(len(p)):
            item = []
            item.append(i + 1)
            item.append(p[i])
            problems.append(item)
        if not name:
            return render(request, "teach/quiz/edit_quiz.html", {"user":user, "lesson":lesson, "quiz":quiz, "problems":problems, "error":"Please choose a name!"})
        try:
            Quiz.objects.filter(pk=quiz_id).update(name=name)
            quiz = get_object_or_404(Quiz, pk=quiz.id)
            quiz.save()
        except:
            return render(request, "teach/quiz/edit_quiz.html", {"user":user, "lesson":lesson, "quiz":quiz, "problems":problems, "error":"Could not update!"})

        i = 1
        while True:
            try:
                question = request.POST["question" + str(i)]
                print(str(i) + " Try **************************")
            except:
                print(str(i) + " Except **************************")
                question = None
            if not question:
                p = Problem.objects.filter(quiz=quiz)
                problems = []
                for i in range(len(p)):
                    item = []
                    item.append(i + 1)
                    item.append(p[i])
                    problems.append(item)
                if len(p) == 0:
                    return render(request, "teach/quiz/edit_quiz.html", {"user":user, "lesson":lesson, "quiz":quiz, "problems":problems, "error":"Create questions for quiz or delete!"})
                quizzes = Quiz.objects.filter(lesson=lesson)
                number_of_quizzes = len(quizzes)
                lesson.number_of_quizzes = number_of_quizzes
                lesson.save()
                number_of_problems = len(p)
                quiz.number_of_problems = number_of_problems
                quiz.save()
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
                        return render(request, "teach/quiz/edit_quiz.html", {"user":user, "lesson":lesson, "quiz":quiz, "problems":problems, "error":"Create answers for all questions!"})
                correct_answer = request.POST["correct_answer" + str(i)]
                problem = Problem.objects.create(teacher = teacher, quiz = quiz, question = question, answers = answers, correct_answer=correct_answer)
                problem = get_object_or_404(Problem, pk=problem.id)
                problem.save()
                i += 1

def take_quiz(request, quiz_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("collections:login")

        quiz = get_object_or_404(Quiz, pk=quiz_id)

        if quiz.teacher.user.id == request.user.id:
            lesson = get_object_or_404(Lesson, pk=quiz.lesson.id)
            p = Problem.objects.filter(quiz=quiz)
            problems = []  # Problems with numbers attached
            for i in range(len(p)):
                item = []
                item.append(i + 1)
                item.append(p[i])
                problems.append(item)
            return render(request, "teach/quiz/take_quiz.html", {"user": user, "lesson": lesson, "quiz": quiz, "problems": problems})
        else:
            return render(request, "teach/index.html",
                          {"error": "You can't take this quiz!"})

def submit_quiz(request, quiz_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("collections:login")

        quiz = get_object_or_404(Quiz, pk=quiz_id)

        lesson = get_object_or_404(Lesson, pk=quiz.lesson.id)
        p = Problem.objects.filter(quiz=quiz)
        problems = []  # Problems with numbers attached
        for i in range(len(p)):
            item = []
            item.append(i + 1)
            item.append(p[i])
            submitted_answer = request.POST["submitted_answer" + str(i + 1)]
            item.append(submitted_answer)
            problems.append(item)
        return render(request, "teach/quiz/quiz_results.html", {"user": user, "lesson": lesson, "quiz": quiz, "problems": problems})

def find_quiz(request):
    if request.method == "POST":
        quiz_id = request.POST["code"]
        try:
            quiz = get_object_or_404(Quiz, pk=quiz_id)
        except:
            quiz = None
        is_base_visible = False
        if quiz:
            user = quiz.teacher
            lesson = get_object_or_404(Lesson, pk=quiz.lesson.id)
            p = Problem.objects.filter(quiz=quiz)
            problems = []  # Problems with numbers attached
            for i in range(len(p)):
                item = []
                item.append(i + 1)
                item.append(p[i])
                problems.append(item)
            return render(request, "teach/quiz/take_quiz.html", {"user": user, "lesson": lesson, "quiz": quiz, "problems": problems})
        else:
            return redirect("collections:code")

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
            Lesson.objects.filter(pk=lesson.id).update(number_of_quizzes=number_of_quizzes)
            return render(request, "teach/quiz/show_all_quizzes.html", {"user":user, "lesson":lesson, "quizzes":quizzes, "number_of_quizzes":number_of_quizzes})

        quizzes = Quiz.objects.filter(lesson=lesson)
        number_of_quizzes = len(quizzes)
        return render(request, "teach/quiz/show_all_quizzes.html", {"user":user, "lesson":lesson, "quizzes":quizzes, "number_of_quizzes":number_of_quizzes, "error":"This is not your quiz!"})
    else:
        return HttpResponse(status=500)

def delete_problem(request, problem_id):
    print("Delete Problem")
    print(problem_id)
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return HttpResponse(status=500)
        problem = get_object_or_404(Problem, pk=problem_id)
        quiz = get_object_or_404(Quiz, pk=problem.quiz.id)
        Problem.objects.get(pk=problem_id).delete()
        problems = Problem.objects.filter(quiz=quiz)
        number_of_problems = len(problems)
        quiz.number_of_problems = number_of_problems
        quiz.save()
        return HttpResponse(status=500)
    else:
        return HttpResponse(status=500)

def switch_public_private(request):
    pass
