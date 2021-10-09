from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images=Image.get_all_images()
    locations=Location.get_locations()

    return render(request, 'all-gallery/home.html',{"images":images,"locations":locations})

def all_locations(request):
    locations=Location.get_locations()
    return render(request,'all-gallery/home.html',{"locations":locations})

def image_by_location(request,location):
    locations=Location.get_locations()
    images=Image.get_image_by_location(location)
    return render(request,'all-gallery/location.html',{"images":images,"location":location,"locations":locations})    
