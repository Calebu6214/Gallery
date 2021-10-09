from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def home(request):
    images=Image.get_all_images()
    locations=Location.get_locations()

    return render(request, 'all-gallery/home.html',{"images":images,"locations":locations})
