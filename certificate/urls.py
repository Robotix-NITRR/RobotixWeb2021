from django.urls import re_path,include, path
from .views import Search, enter_id
urlpatterns = [
    # re_path(r'^(?P<url_key>[0-9a-f-]+)/',Search,name='search'),
    path('<uuid:url_key>/', Search, name='search'),
    path('', enter_id, name='enter_id'),
]

