from django.urls import path
from . import views
app_name = 'workshops'
urlpatterns = [
    path('recruitment-2021/',views.recruitment_view,name='recruitment')
]
