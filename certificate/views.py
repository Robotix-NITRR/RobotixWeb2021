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
                return redirect('search', url_key=url_key)

            return render(request, "certificate/certificate.html", {'certificate':obj})

        elif request.method == 'POST':
            # form = CertificateForm(request.POST)
            url_key = request.POST.get('url_key')
            return redirect('search', url_key=url_key,)

        else:
            return render(request, "certificate/certificate.html")

    except NoReverseMatch:
        request_obj = True     ## This is for Invalid sign that pops up if the id is invalid
        return render(request, "certificate/certificate.html", {'request_obj':request_obj},)


from .models import Certificate
#emalis
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
#PIL
from PIL import Image, ImageDraw
#utill
import requests
import tempfile
from django.core import files
import os
import time

def send_mails(request):
    objs = Certificate.objects.filter(email_sent=False)
    for obj in objs:
        html_content = '<h3>This is an sample yet <strong>important</strong> message to all the participants.</h3>'
        msg = EmailMultiAlternatives(
            'Get your certificate',               # subject,
            'Download this certificate here!',      # text_content,
            'robotixclub@nitrr.ac.in',                # from_email,
            ['{}'.format(obj.email),],             # to email(s)
        )
        msg.attach_alternative(html_content, "text/html")
        msg.attach_file('media/{}'.format(obj.image))
        msg.send()
        obj.email_sent=True
        obj.save()
    return render(request, "certificate/certificate.html")

def create_image(request):
    objs = Certificate.objects.filter(image_created=False)
    image_url = "https://robotix.nitrr.ac.in/static/img/cert.jpg"
    response = requests.get(image_url, stream=True)
    for obj in objs:
        if obj.image_created:
            file_name = image_url.split('/')[-1]
            lf = tempfile.NamedTemporaryFile()
            for block in response.iter_content(1024 * 8):
                if not block:
                    break
                lf.write(block)
            my_img = Image.open(lf)
            d1 = ImageDraw.Draw(my_img)
            name = str(obj.name)
            event_name = str(obj.event.title)
            d1.text((460, 410), name,  fill="black")
            d1.text((400, 270), event_name,  fill="black")
            new_img_temp_file = tempfile.NamedTemporaryFile(suffix = '.jpeg')
            my_img.save(new_img_temp_file)

            obj.image_created=True
            obj.image.save(file_name, files.File(new_img_temp_file))
            obj.save()
    return render(request, "certificate/certificate.html")