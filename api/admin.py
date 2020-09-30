from django.contrib import admin
from .models import User, Profile, Education, Experience

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)