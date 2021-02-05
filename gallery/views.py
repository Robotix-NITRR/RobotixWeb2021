from django.shortcuts import render
from .models import Gallery
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GallerySerializer
# Create your views here.

@api_view()
def gallery_api(request):
    obj_gallery = Gallery.objects.all()
    serializer = GallerySerializer(obj_gallery,many=True)
    dict = {'gallery':serializer.data}
    # return render(request,'gallery.html',context=dict)
    return Response(dict)


def gallery(request):
    obj_gallery = Gallery.objects.all()
    # serializer = GallerySerializer(obj_gallery,many=True)
    dict = {'gallery':obj_gallery}
    return render(request,'gallery-page.html',context=dict)
    # return Response(dict)
