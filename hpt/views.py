from django.shortcuts import render
from django.http import HttpResponse  
# Create your views here.
def index(request):
    return render(request,"index.html")


def blue(request):
     request.method=="POST"

def red(request):
     request.method=="POST"