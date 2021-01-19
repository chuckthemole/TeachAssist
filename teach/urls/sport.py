from django.urls import path, include
from teach.views import sport  #import everything from views module
app_name = 'teach'

urlpatterns = [
    # sport
    path('sport/publish', sport.publish_create_sport, name='publish_create_sport'),
    path('sport/create', sport.create_sport, name='create_sport'),
]
