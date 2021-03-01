from django.conf.urls import url
from django.db.models.signals import post_delete
from django.shortcuts import redirect, render,HttpResponse
from django.shortcuts import get_object_or_404
from django.urls.exceptions import NoReverseMatch
from .models import Certificate
from .forms import CertificateForm


def Search(request,url_key=None):
    try:
        if url_key != None:

            obj = get_object_or_404(Certificate,url_key=url_key)
            if request.method == 'POST':
                # form = CertificateForm(request.POST)
                url_key = request.POST.get('url_key')
                return redirect('certificate:search', url_key=url_key)

            return render(request, "certificate/certificate.html", {'certificate':obj})

        elif request.method == 'POST':
            # form = CertificateForm(request.POST)
            url_key = request.POST.get('url_key')
            return redirect('certificate:search', url_key=url_key,)

        else:
            return render(request, "certificate/certificate.html")

    except NoReverseMatch:
        request_obj = True     ## This is for Invalid sign that pops up if the id is invalid
        return render(request, "certificate/certificate.html", {'request_obj':request_obj},)
