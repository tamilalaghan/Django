from django.urls import path

from notes import views

urlpatterns = [
    path("notes",views.notes),
    path("notes/<int:pk>",views.notesdetail)
]