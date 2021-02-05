from django.urls import path
from . import views
urlpatterns = [
    path('',views.achievement,name='achievement'),
    path('api/',views.achievement_api,name='achievement_api')

]
