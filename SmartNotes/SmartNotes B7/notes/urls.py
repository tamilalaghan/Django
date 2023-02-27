from django.urls import path

from notes import views

urlpatterns=[
    path("notes",views.noteslist),
    path("notes/<int:pk>",views.notes)
]