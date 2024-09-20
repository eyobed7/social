from django.contrib import admin
from .models import User,Profile
from django.contrib.auth.admin import UserAdmin as default


class UserAdmin(default):
    list_display=('email','username')


admin.site.register(User,UserAdmin)
admin.site.register(Profile)
