from django.shortcuts import render
from .models import Contact
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializer
# Create your views here.

@api_view(['GET','POST'])
def contact_api(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['email'] and request.POST['message']:
            obj_contact = Contact()
            obj_contact.name = request.POST['name']
            obj_contact.email = request.POST['email']
            obj_contact.message = request.POST['message']
            obj_contact.save()
            # return render(request,'contact.html')
            dict = {'message' : 'Got Data!', 'data': request.data}
            return Response(dict)

    else:
        return render(request,'contact.html')

def contact(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['email'] and request.POST['message']:
            obj_contact = Contact()
            obj_contact.name = request.POST['name']
            obj_contact.email = request.POST['email']
            obj_contact.message = request.POST['message']
            obj_contact.save()
            return render(request,'contact.html')
            # dict = {'message' : 'Got Data!', 'data': request.data}
            # return Response(dict)

    else:
        return render(request,'contact.html')
