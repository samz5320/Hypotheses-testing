from django.shortcuts import render
from django.http import HttpResponse
from .models import Red, Blue
from .hypo1 import Hypo1
from .mean import Mean
# Create your views here.
def index(request):
     red = len(Red.objects.all())
     blue = len(Blue.objects.all())
     m = Mean()
     print(m.blue_time)
     h=Hypo1()
     print(h.op)
     count = {
          "red":red,
          "blue":blue,
          "op": h.op
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

#def hypotest(request)
#if request.method="POST":
#     h=hypo1
#

