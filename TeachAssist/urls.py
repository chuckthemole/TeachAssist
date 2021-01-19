"""TeachAssist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teach.urls.collections', namespace='collections')),
    path('', include('teach.urls.comment', namespace='comment')),
    path('', include('teach.urls.destination', namespace='destination')),
    path('', include('teach.urls.lesson', namespace='lesson')),
    path('', include('teach.urls.location', namespace='location')),
    path('', include('teach.urls.map', namespace='map')),
    path('', include('teach.urls.review', namespace='review')),
    path('', include('teach.urls.sport', namespace='sport')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
