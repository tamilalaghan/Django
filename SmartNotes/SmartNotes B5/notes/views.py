from django.shortcuts import render

# Create your views here.
from notes.models import Notes
def notes(request):
    all_notes = Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes':all_notes})