
from django.urls import path
from . import views
urlpatterns = [
    path('',views.about,name='about'),
    path('api/',views.about_api,name='about_api')
]
