from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('',views.home,name = 'home'),
    path('location/<location>/',views.image_by_location,name='location'),
    url(r'search/',views.search_by_category,name='search'),
    path('image/<int:image_id>/',views.single_image,name='image'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)