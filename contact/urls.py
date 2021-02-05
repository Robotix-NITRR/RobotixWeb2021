from django.urls import path
from . import views
urlpatterns = [
    path('',views.contact,name='contact'),
    path('api/',views.contact_api,name='contact_api')
]
