from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
	path('get_upload_lost_person_image_form', get_upload_lost_person_image_form, name='get_upload_lost_person_image_form'),
	path('upload_lost_person_image_form', upload_lost_person_image_form, name='upload_lost_person_image_form')
]