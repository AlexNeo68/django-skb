from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .forms import UserBioForm

def index(request:HttpRequest)->HttpResponse:
    context = {
        'a': request.GET.get('a'),
        'b': request.GET.get('b'),
        'result': request.GET.get('a') + request.GET.get('b')
    }
    return render(request, 'requestapp/index.html', context)

def handle_post(request:HttpRequest):
    context = {
        'form': UserBioForm(),
    }
    return render(request, 'requestapp/post.html', context)

def handle_file(request:HttpRequest)->HttpResponse:
    filename = ''
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
    
    context = {
        'filename': filename
    }  
    return render(request, 'requestapp/handle_file.html', context)
