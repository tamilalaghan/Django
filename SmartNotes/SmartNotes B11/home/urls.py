from django.urls import path
from home import views
urlpatterns = [
    #uncomment for Function based view patterns
    # path("home",views.home),
    # path("authorized",views.authorized)

    #lets look at including class based patterns
    path("home",views.HomeView.as_view()),
    path("authorized",views.AuthorizedView.as_view())
]