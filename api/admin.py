from django.contrib import admin
from .models import User, Profile, Education, Experience, Feed, FriendRequest

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Feed)
admin.site.register(FriendRequest)