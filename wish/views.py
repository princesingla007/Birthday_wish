from django.shortcuts import render,redirect
from . models import Img,Cake

# Create your views here.

def index(request):
    return render(request,"index.html")

def puzzel(request):
    images=Img.objects.all()
    return render(request,"puzzel.html",{"images":images})

def cake_cut(request):
    img=Cake.objects.all()
    return render(request,"cake_cut.html",{"img":img})

def surprise_box(request):
    return render(request,"surprise_box.html")

def balloon(request):
    return render(request,"balloon.html")

def last(request):
    return render(request,"last.html")