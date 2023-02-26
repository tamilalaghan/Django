from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home/welcome.html',{'randomnumber':random.randint(10000,99999)})

@login_required(login_url="/admin")
def authorized(request):
    return render(request,'home/authorized.html',{})