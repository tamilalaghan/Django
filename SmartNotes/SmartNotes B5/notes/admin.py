from django.contrib import admin

# Register your models here.
from notes.models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title','created')

admin.site.register(Notes,NotesAdmin)