from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request,"home/welcome.html",{"randomnumber":random.randint(100000,999999)})
