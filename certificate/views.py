from django.conf.urls import url
from django.db.models.signals import post_delete
from django.shortcuts import redirect, render,HttpResponse
from django.shortcuts import get_object_or_404
from .models import Certificate
from .forms import CertificateForm

def Search(request,url_key):
    obj = get_object_or_404(Certificate,url_key=url_key)

    if request.method == 'POST':
        # form = CertificateForm(request.POST)
        url_key = request.POST.get('url_key')
        return redirect('search', url_key=url_key)

    return render(request, "certificate/certificate2.html", {'certificate':obj})



def enter_id(request):

    if request.method == 'POST':
        # form = CertificateForm(request.POST)
        url_key = request.POST.get('url_key')
        return redirect('search', url_key=url_key)
    else:
        form = CertificateForm()
    return render(request, "certificate/certificate.html")
    