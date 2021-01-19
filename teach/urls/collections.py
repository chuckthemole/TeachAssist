from django.urls import path, include
from teach.views import collections
app_name = 'teach'

urlpatterns = [
    path('',collections.index, name='index'),
    path('dashboard', collections.dashboard, name='dashboard'),

    path('create', collections.create, name='create'),
    path('loguser', collections.login_user, name='loguser'),
    path('login', collections.login_view, name='login'),
    path('logout', collections.logout_view, name='logout'),
    path('signup', collections.signup, name='signup'),
]
