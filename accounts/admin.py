from django.contrib import admin

# Register your models here.
from .models import City, Profile

admin.site.register(City)
admin.site.register(Profile)
