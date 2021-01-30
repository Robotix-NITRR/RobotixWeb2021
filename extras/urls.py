from django.urls import path
from . import views
app_name = 'info'
urlpatterns = [
    path('diy/',views.diy,name='diy'),
    path('fyi/',views.fyi,name='fyi'),
    path('diy/api/',views.diy_api,name='diy_api'),
    path('fyi/api/',views.fyi_api,name='fyi_api'),
    path('sponsors/',views.sponsors,name='sponsors')
]
