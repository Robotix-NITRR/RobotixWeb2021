
from django.urls import path
from . import views
urlpatterns = [
    path('',views.event,name='event'),
    path('api/',views.event_api,name='event_api')
]
