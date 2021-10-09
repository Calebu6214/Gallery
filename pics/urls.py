from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('image_location/<location>/',views.image_by_location,name='image_by_location'),
    url('search/',views.search_by_category,name="search"),
    url('image/<int:image_id>/',views.single_image,name='image')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)