from django.contrib import admin

from .models import UserInfo, ProgrammingLanguages, Sports

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(ProgrammingLanguages)
admin.site.register(Sports)
