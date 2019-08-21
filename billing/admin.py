from django.contrib import admin
from .models import Company, BillHeader, BillLines


admin.site.register(Company)
admin.site.register(BillHeader)
admin.site.register(BillLines)
