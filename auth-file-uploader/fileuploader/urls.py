from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
  
app_name = 'fileuploader'


urlpatterns = [
    path('', image_upload_view, name = 'file_upload'),
    path('success', success, name = 'success'),
]
  
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)