from django.shortcuts import render
from django.http import HttpRequest
from django.http import Http404

# Create your views here.
from notes.models import Notes

def noteslist(request):
    notes_list = Notes.objects.all()
    return render(request,"notes/notes_list.html",{'notes_list':notes_list})

def notes(request,pk):
    try :
        note = Notes.objects.get(pk = pk)
        return render(request,"notes/notes_details.html",{'note':note})
    except Notes.DoesNotExist:
        raise Http404("The Request Could Not be completed")



