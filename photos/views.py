from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    return render(request, 'all-photos/index.html',{"images":images,})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET("category")
        searched_categories = Image.search_by_category(search_term)
        
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html',{"message":message,"categories":searched_categories})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message,"categories":searched_categories})
        