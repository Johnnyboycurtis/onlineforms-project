from django.contrib import admin

from .models import UserInfo, ProgrammingLanguages, Sports

# Register your models here.
admin.site.Register(UserInfo)
admin.site.Register(ProgrammingLanguages)
admin.site.Register(Sports)
