from django.shortcuts import render
from django.http import Http404

# Create your views here.
from notes.models import Notes
def notes(request):
    all_notes = Notes.objects.all()
    return render(request,'notes/notes_list.html',{'notes':all_notes})

def notesdetail(request,pk):
    try :
        notes_detail = Notes.objects.get(pk = pk)
        return render(request,'notes/notes_details.html',{'notes_detail':notes_detail})
    except Notes.DoesNotExist:
        raise Http404 ("Notes Doesn't exist")
