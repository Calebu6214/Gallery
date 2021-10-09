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

def search_by_category(request):
    categories=Category.objects.all()
    locations=Location.objects.all()
    
    if 'category' in request.GET and request.GET["category"]:
        search_term=request.GET.get("category")
        searched_categories=Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'all-gallery/search.html',{"message":message,"searched_categories":searched_categories,"categories":categories,"locations":locations})
    
    else:
        message ="You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message}) 

def single_image(request,image_id):
    try:
        image=Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request,"all-gallery/image.html",{"image":image})   
