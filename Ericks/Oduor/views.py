from django.shortcuts import render
from .models import stuffs

# Create your views here.

def home(request):
    Details = stuffs.objects.all()
    return render(request,'index.html',{'Details':Details})

