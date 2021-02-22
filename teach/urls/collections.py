from django.urls import path, include
from teach.views import collections
app_name = 'teach'

urlpatterns = [
    path('',collections.index, name='index'),
    path('dashboard', collections.dashboard, name='dashboard'),
    path('about', collections.about, name='about'),
    path('create', collections.create, name='create'),
    path('loguser', collections.login_user, name='loguser'),
    path('login', collections.login_view, name='login'),
    path('logout', collections.logout_view, name='logout'),
    path('signup', collections.signup, name='signup'),
    path('settings', collections.edit_settings, name='edit_settings'),
    path('search', collections.search, name='search'),
    path('<int:teacher_id>/publish', collections.publish_settings, name='publish_settings'),
    path('filter', collections.index_filter, name='index_filter'),
    path('student', collections.student, name='student'),
]
