from django.contrib import admin
from django.db import models
from .models import Profile, Machine

admin.site.register(Profile)
admin.site.register(Machine)
