from django.contrib import admin
from . models import User, Profile, Questions, Scores

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Questions)
admin.site.register(Scores)
