from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location,Category

# Create your views here.
def index(request):
    category=request.GET.get('category')
    images=Image.objects.all()  
    categories=Category.objects.all()
    return render(request, 'personalgallery/index.html', {"images":images, "categories": categories})

def show_category(request):
    if 'article' in request.GET and request.GET['article']:
        category=request.GET.get("article")
        searched_categories=Image.search_image(category)
        message=f"{category}"

        return render(request, 'personalgallery/search.html', {"message": message, "articles": searched_categories })
    else:
        message="You have not searched any category"
        return render(request, 'personalgallery/search.html', {"message":message})