from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location,Category

# Create your views here.
def index(request):
    images=Image.objects.all()  
    return render(request, 'personalgallery/index.html', {"images":images})
