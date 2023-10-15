from django.shortcuts import render, redirect
from .models import stuffs
from .addstuffsform import addStuffs
from django.http import HttpResponse

# Create your views here.

def home(request):
    Details = stuffs.objects.all()
    return render(request,'index.html',{'Details':Details})

def addStuffsView(request):
    form = addStuffs()
    if request.method == "POST":
        form = addStuffs(request.POST)
        if form.is_valid():
            model_instance = stuffs(
                name_of_tool = form.cleaned_data['name_of_tool'],
                description =  form.cleaned_data['description'],
                tutorial_tool =  form.cleaned_data['tutorial_tool'],
                ad =  form.cleaned_data['ad'],
                youtube_link =  form.cleaned_data['youtube_link'],
            )
            model_instance.save()
            return HttpResponse('Tool Added successfully')
        else:
            form = addStuffs()

    return render (request, 'Addstuffsform.html', {'form':form})

