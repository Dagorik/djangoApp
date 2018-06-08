from django.contrib import admin
from .models import Kind_Company

class KindCompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Kind_Company, KindCompanyAdmin)

