from django.contrib import admin
from .models import Reports

class ReportAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reports, ReportAdmin)
