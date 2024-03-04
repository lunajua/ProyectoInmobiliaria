from django.contrib import admin
from users.models import Avatar
from django.contrib.auth.models import User
# Register your models here.


admin.site.register(User)
admin.site.register(Avatar)