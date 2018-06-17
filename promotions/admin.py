from django.contrib import admin
from .models import Promotions

class PromotionsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Promotions,PromotionsAdmin)