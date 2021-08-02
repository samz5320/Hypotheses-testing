from django.shortcuts import render
from django.http import HttpResponse
from .models import Red, Blue

from .mean import Mean
# Create your views here.
def index(request):
     red = len(Red.objects.all())
     blue = len(Blue.objects.all())
     m = Mean()
     print(m.blue_time)
     
     count = {
          "red":red,
          "blue":blue
     }

     return render(request,"index.html", context=count)


def blue(request):
     if request.method=="POST":
          data = request.POST
          time = data['time']
          Blue.objects.create(count=1, time=time)
     return HttpResponse("<h2>OK</h2>")

def red(request):
     if request.method=="POST":
          data = request.POST
          time = data['time']
          Red.objects.create(count=1, time=time)
     return HttpResponse("<h2>OK</h2>")