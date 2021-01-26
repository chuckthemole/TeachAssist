from .imports import *

# Locations
def publish_lesson(request):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            form = Lesson_Form()
            return render(request, "teach/lesson/create_lesson.html", {"user":user, "form":form} )

def create_lesson(request):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")

        teacher = user.teacher
        subject = request.POST["subject"]
        subject_class = request.POST["choices"]
        lesson_name = request.POST["name"]
        lesson_description = request.POST["description"]
        public_private = request.POST["is_public"]

        if public_private == 'public':
            is_public = True
        else:
            is_public = False
        if not subject or not subject_class:
            return render(request, "teach/lesson/create_lesson.html", {"error":"Please choose a subject and class!"})

        if subject == 'math':
            icon = 'https://img.icons8.com/dusk/64/000000/math.png'
        elif subject == 'science':
            icon = 'https://img.icons8.com/dusk/64/000000/bunsen-burner.png'
        elif subject == 'history':
            icon = 'https://img.icons8.com/dusk/64/000000/archeology.png'
        elif subject == 'english':
            icon = 'https://img.icons8.com/dusk/64/000000/class.png'
        else:
            icon = 'https://img.icons8.com/dusk/50/000000/book-and-pencil.png'

        # Geocoding an address
        #address = request.POST["address"]
        #zip = request.POST["zip"]
        #gmaps = googlemaps.Client(key='AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko')
        #geocode_result = gmaps.geocode(address + " " + zip)
        #df = DataFrame (geocode_result)
        #loc = DataFrame (df['geometry'][0])

        # Sometimes the DF is missing values. Try first two if they exist
        #if str(loc['location'][0]) != 'nan' and str(loc['location'][1]) != 'nan':
        #    latitude = float(loc['location'][0])
        #    longitude = float(loc['location'][1])
        #else:
        #    latitude = float(loc['location'][2])
        #    longitude = float(loc['location'][3])

        #print("( LATITUDE: " + str(latitude) + ", LONGITUDE: " + str(longitude) + " )")

        # Make more requirements for adress inputs
        #if address == "" or len(zip) < 5:
        #    return render(request, "teach/lesson/create_lesson.html", {"error":"Enter a proper address"})

        try:
            lesson = Lesson.objects.create(
                teacher = teacher,
                subject = subject,
                subject_class = subject_class,
                lesson_name = lesson_name,
                description = lesson_description,
                topic = 'this',
                is_public = is_public,
                icon = icon
                #sport_location_img='images/no_image_available.PNG',
                #latitude=latitude, longitude=longitude,
                #teacher=teacher, address=address, zip=zip,
                #sport=sport, is_basketball=is_basketball,
                #is_tennis=is_tennis, is_baseball=is_baseball
                )

            lesson = get_object_or_404(Lesson, pk=lesson.id)
            form = Lesson_Form(request.POST, request.FILES, instance=lesson)
            if form.is_valid():
                print("Form is valid.")
                lesson.save()
            else:
                print("Form is not valid!")

            return render(request, "teach/lesson/show_lesson.html", {"user":user, "lesson":lesson})
        except:
            print("*******Returning to create_lesson.html error*********")
            return render(request, "teach/lesson/create_lesson.html", {"error":"Can't create the lesson"})
    else:
        user = request.user
        all_lessons = Lesson.objects.all()
        return render(request, "teach/index.html", {"user":user, "all_lessons": all_lessons, "error":"Can't create!"})

def show_lesson(request, lesson_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            return render(request, "teach/lesson/show_lesson.html", {"user":user, "lesson":lesson})

def publish_image(request, location_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            location = get_object_or_404(Lesson, pk=lesson_id)
            form = Sport_Location_Form()
            return render(request, "teach/lesson/show_map.html", {"user":user, "lesson":lesson, "form":form} )

def create_image(request, lesson_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            try:
                lesson = get_object_or_404(Lesson, pk=lesson_id)
                form = Sport_Location_Form(request.POST, request.FILES, instance=lesson)
            except:
                return render(request, "teach/lesson/show_map.html", {"error":"Error"})
            if form.is_valid():
                #form.save()
                #upload = Upload(file=location.sport_location_img)
                #upload.save()
                #location.img_url = str(upload.file.url)
                lesson.save()
                return render(request, "teach/lesson/show_lesson.html", {"user":user, "lesson":lesson} )
            else:
                form = Sport_Location_Form()
                return render(request, "teach/lesson/show_map.html", {"error":"Error"})
    else:
        if request.user.is_authenticated:
            user = request.user
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            return render(request, "teach/lesson/show_lesson.html", {"user":user, "lesson":lesson})
        else:
            return redirect("teach:login")

def show_image(request, lesson_id):
    if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("teach:login")
        else:
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            return render(request, "teach/lesson/show_image.html", {"user":user, "lesson":lesson})

def edit_lesson(request, lesson_id):
   if request.method == "GET":
        user = request.user
        if not user.is_authenticated:
            return redirect("share:login")

        lesson = get_object_or_404(Lesson, pk=lesson_id)
        form = Lesson_Form()

        if lesson.teacher.user.id == lesson.teacher.user.id:
            return render(request, "teach/lesson/edit_lesson.html", {"lesson":lesson, "form":form})
        else:
            return render(request, "teach/index.html",
            {"error":"You are not the author of the lesson that you tried to edit."})

def update_lesson(request, lesson_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return HttpResponse(status=500)

        lesson = get_object_or_404(Lesson, pk=lesson_id)

        if 'subject' in request.POST and 'subject_class' in request.POST:
            try:
                subject = request.POST["subject"]
                subject_class = request.POST["choices"]
                lesson_name = request.POST["name"]
                lesson_description = request.POST["description"]
                public_private = request.POST["is_public"]

                if public_private == 'public':
                    is_public = True
                else:
                    is_public = False
            except:
                return render(request, "teach/lesson/edit_lesson.html", {"error":"Error updating lesson!"})
            if lesson.teacher.user.id == user.id:
                Lesson.objects.filter(pk=lesson_id).update(subject=subject, subject_class=subject_class, lesson_name=lesson_name,
                    description=lesson_description, is_public=is_public)
                return render('GET', "teach/lesson/show_lesson.html", {"user":user, "lesson":lesson})
            else:
                return render(request, "teach/lesson/edit_lesson.html",{"lesson":lesson, "error":"Can't update!"})
        else:
            return render(request, "teach/lesson/edit_lesson.html", {"lesson":lesson, "error":"One of the required fields was empty"})
    else:
        user = request.user
        all_lessons = Lesson.objects.all()
        return render(request, "teach/index.html", {"user":user, "all_lessons": all_lessons, "error":"Can't update!"})

def delete_lesson(request, lesson_id):
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            return HttpResponse(status=500)

        lesson = get_object_or_404(Lesson, pk=lesson_id)

        if lesson.teacher.user.id == user.id:
            lesson.img.delete(save=False)  # Deletes the file from AWS S3
            Lesson.objects.get(pk=lesson_id).delete()   # Deletes Location instance
            return redirect("collections:dashboard")
        else:
            all_lessons = Lesson.objects.all()
            return render(request, "teach/index.html", {"user":user, "all_lessons": all_lessons, "error":"Can't delete!"})

    else:
        return HttpResponse(status=500)
