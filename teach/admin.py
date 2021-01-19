from django.contrib import admin
from .models import teacher, Sport, Location, Destination, Review, Comment

admin.site.register(teacher)
admin.site.register(Location)
admin.site.register(Destination)
admin.site.register(Review)
admin.site.register(Comment)
