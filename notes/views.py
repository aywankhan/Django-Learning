from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes


# Create your views here.
class NotesListView(ListView):
    model = Notes
    context_object_name = "noets"
    template_name = "notes/notes_list_html"

'''
def List(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {"notes": all_notes})
'''

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_details.html"

'''
def Details(request, pk):
    try:
        all_notes = Notes.objects.get(pk = pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_details.html', {"notes": all_notes})
'''