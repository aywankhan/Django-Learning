from django.urls import path
from . import views

urlpatterns = [
    path("notes", views.NotesListView.as_view(), name="notes_list"),
    path("notes/<int:pk>", views.NotesDetailView.as_view(), name="notes_details"),
    path("new", views.CreateNoteView.as_view(), name="notes_new"),
]
