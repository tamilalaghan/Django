from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    r1 = random.randint(100000,999999)
    return render(request,'home/welcome.html',{'randomnumber':r1})
