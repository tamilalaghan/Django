from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

# Create your views here.


def home(request):
    r1 = random.randint(5000,8000)
    currentTime = datetime.now()
    return render(request,'home/welcome.html',
                  {'randomnumber' : r1, 'time': currentTime.strftime("%H:%M:%S")})