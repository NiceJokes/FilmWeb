from django.contrib import admin
from .models import Movie,Person,Role,Vote

# Register your models here.
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Vote)