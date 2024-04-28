from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def upload_audio(request):
    return render(request, 'upload_audio.html')
