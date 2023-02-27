from django.urls import path

from notes import views

urlpatterns=[
    path("notes",views.NotesView.as_view()),
    path("notes/<int:pk>",views.NotesDetailView.as_view())
]