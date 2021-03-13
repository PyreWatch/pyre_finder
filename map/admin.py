from django.contrib import admin
from .models import Fighter

# Register your models here.
@admin.register(Fighter)
class FighterAdmin(admin.ModelAdmin):
    list_display = ("id", "latitude", "longitude", "fire_status", "operation_status")