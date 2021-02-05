from django.urls import path
from . import views
urlpatterns = [
    path('',views.alumni,name='alumni'),
    path('api/',views.alumni_api,name='alumni_api')
]
