
from django.urls import path
from . import views
urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('api/',views.gallery_api,name='gallery_api')
]
