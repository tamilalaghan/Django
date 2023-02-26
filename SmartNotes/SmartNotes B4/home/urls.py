from django.urls import path

#import views.py from home app
from home import views

urlpatterns =[
    path("home",views.home),
    path("authorized",views.authorized)
]
