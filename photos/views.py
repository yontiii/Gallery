from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    return render(request, 'all-photos/index.html',{"images":images,})
