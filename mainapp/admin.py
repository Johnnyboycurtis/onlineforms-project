from django.contrib import admin

from .models import Contacts, ProgrammingLanguages, Sports

# Register your models here.
admin.site.register(Contacts)
admin.site.register(ProgrammingLanguages)
admin.site.register(Sports)
