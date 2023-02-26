from django.contrib import admin

# Register your models here.
from notes import models

class AdminNotes(admin.ModelAdmin):
    list_display = ('title','created')

admin.site.register(models.Notes,AdminNotes)

