from django.urls import path
from home import views

urlpatterns =[
    #home function under home/views.py
    path('home', views.home),
    #views function under home/views.py
    path('authorized', views.authorized)
]