from django.urls import path
from . import views
app_name = 'roboexpo'
urlpatterns = [
    path('registration/', views.expo, name='roboexpo-registration'),
]
