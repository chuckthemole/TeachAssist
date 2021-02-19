from .imports import *
from ..static.teach.py.constants import *

def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user = request.user
            all_lessons = Lesson.objects.filter(is_public=True)
            all_icons = [MATH_ICON, SCIENCE_ICON, ENGLISH_ICON, HISTORY_ICON]
            no_lessons = True
            if len(all_lessons) != 0:
                no_lessons = False
            return render(request, "teach/index.html", {"user":user, "all_lessons": all_lessons, "all_icons": all_icons, "no_lessons": no_lessons})
        else:
            return redirect("collections:login")
    else:
        return HttpResponse(status=500)

def index_filter(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            subject = request.POST["subject"]
        user = request.user
        if subject != "all":
            all_lessons = Lesson.objects.filter(is_public=True, subject=subject)
        else:
            all_lessons = Lesson.objects.filter(is_public=True)
        all_icons = [MATH_ICON, SCIENCE_ICON, ENGLISH_ICON, HISTORY_ICON]
        no_lessons = True
        if len(all_lessons) != 0:
            no_lessons = False
        return render(request, "teach/index.html", {"user":user, "all_lessons": all_lessons, "all_icons": all_icons, "no_lessons": no_lessons})
    else:
        return HttpResponse(status=500)

def dashboard(request):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("collections:login")
        else:
            try:
                my_lessons = Lesson.objects.filter(teacher=user.teacher.id)
            except:
                return redirect("collections:login")
            no_lessons = True
            if len(my_lessons) != 0:
                no_lessons = False
            return render(request, "teach/dashboard.html", {"user":user, "my_lessons": my_lessons, "no_lessons": no_lessons})

def create(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        is_base_visible = False
        all_lessons = Lesson.objects.all()

        if username is not None and email is not None and password is not None: # checking that they are not None
            if not username or not email or not password: # checking that they are not empty
                return render(request, "teach/signup.html", {"error": "Please fill in all required fields", "is_base_visible":is_base_visible})
            if User.objects.filter(username=username).exists():
                return render(request, "teach/signup.html", {"error": "Username already exists", "is_base_visible":is_base_visible})
            elif User.objects.filter(email=email).exists():
                return render(request, "teach/signup.html", {"error": "Email already exists", "is_base_visible":is_base_visible})

            user = User.objects.create_user(username, email, password)
            teacher_user = teacher.objects.create(user=user)
            teacher_user.save()
            user.save()

            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            # this logs in our new user, backend means that we are using the  Django specific auhentication and not 3rd party

        return redirect("collections:index")

    else:
        return redirect("collections:signup")

def signup(request):
    if request.user.is_authenticated:
        return redirect("collections:index")
    else:
        is_base_visible = False
        return render(request, 'teach/signup.html', {'is_base_visible':is_base_visible})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        all_lessons = Lesson.objects.all()
        is_base_visible = False
        if not username or not password:
            return render(request, "teach/login.html", {"error":"One of the fields was empty", "is_base_visible":is_base_visible, "all_lessons":all_lessons})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("collections:index")
        else:
            return render(request, "teach/login.html", {"error":"Wrong username or password", "all_lessons":all_lessons, "is_base_visible":is_base_visible})
    else:
        return redirect("collections:index")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("collections:index")
    else:
        is_base_visible = False

        all_lessons = Lesson.objects.all()
        coordinates = []

        if len(all_lessons) != 0:
            return render(request, "teach/login.html", {"all_lessons": all_lessons,
            'is_base_visible':is_base_visible, "lesson": all_lessons[0]})
        else:
            return render(request, "teach/login.html", {"all_lessons": all_lessons, 'is_base_visible':is_base_visible})

        return render(request, 'teach/login.html', {'is_base_visible':is_base_visible})

def logout_view(request):
    logout(request)
    return redirect("collections:login")

def edit_settings(request):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            form = Teacher_Form()
            return render(request, "teach/edit_profile.html", {"user":user, "form":form} )

def publish_settings(request, teacher_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
    teach = get_object_or_404(teacher, pk=user.teacher.id)
    form = Teacher_Form(request.POST, request.FILES, instance=teach)
    if form.is_valid():
        print("Form is valid.")
        teach.save()
    else:
        print("Form is not valid!")
    try:
        my_lessons = Lesson.objects.filter(teacher=user.teacher.id)
    except:
        return redirect("collections:login")
    return render(request, "teach/dashboard.html", {"user":user, "my_lessons":my_lessons})

def code(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("collections:index")
        else:
            is_base_visible = False
        return render(request, "teach/student_login.html", {"is_base_visible":is_base_visible})
    else:
        return HttpResponse(status=500)

def testHTTP_request(request):
    # Testing http request object inside a view function
    print('********************************************')
    print('*********** Testing request obj ************')
    print('*********** request:' , request)
    print('*********** request.headers: ', request.headers)
    print('*********** request.headers["host"]:', request.headers['host'])
    print('*********** request.method: ', request.method)
    print('*********** request.user:' , request.user)
    print('********************************************')
    print('********************************************')
