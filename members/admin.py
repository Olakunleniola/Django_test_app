from django.contrib import admin
from .models import Member
# Register your models here.

class MemAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "joined_date")

admin.site.register(Member,MemAdmin)
