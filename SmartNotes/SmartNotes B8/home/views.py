from django.shortcuts import render
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required

#Adding Template View
from django.views.generic import TemplateView

#Adding Login Mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# Uncomment for Function based Views
# def home(request):
#     return render(request,"home/welcome.html",{'randomnumber':random.randint(100000,999999)})

#lets look at class based views
class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {'randomnumber':random.randint(100000,999999)}

# Uncomment for Function based Views
# @login_required(login_url="admin/")
# def authorized(request):
#     return render(request,"home/authorized.html",{})

#lets look at class based views, remember to pass the Mixin before the Template View
class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = "home/authorized.html"


#comments 
#one thing to note that, when you refresh the page for welcome.html the random lucky number won't chnage again