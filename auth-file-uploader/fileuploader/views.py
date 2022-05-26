from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def image_upload_view(request):

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = UploadForm(request.POST)
            return render(request, 'uploadforms/form.html', {'form': form})
    else:
        form = UploadForm()
    return render(request, 'uploadforms/form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
