from .models import Certificate
#emalis
from django.core.mail import send_mail
from django.conf import settings
#PIL
from PIL import Image, ImageDraw
#utill
import requests
import tempfile
from django.core import files
import os

def cert_job():
    objs = Certificate.objects.all().filter(image_created=False)[:2]
    image_url = "https://robotix.nitrr.ac.in/static/img/cert.jpg"
    #font_url = "http://127.0.0.1:8000/static/font/Raleway-Regular.ttf"
    response = requests.get(image_url, stream=True)
    if response.status_code != requests.codes.ok:
        pass
    else:
        for obj in objs:
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

            obj.image_created = True
            obj.image.save(file_name, files.File(new_img_temp_file))
            obj.save()

def email_job():
    objs = Certificate.objects.all().filter(image_created=True)
    for obj in objs:
        if(obj.image_created == True):
            if(obj.email_sent == False):
                html_content='<h3>This is an sample yet <strong>important</strong><img src="https://robotix.nitrr.ac.in{0}" alt="##"> message to all the participants.</h3>'.format(obj.image.url)
                send_mail(
                    'Subject here',
                    'Here is the message.',
                    'wandavision5432@gmail.com',
                    ['{}'.format(obj.email)],
                    fail_silently=False,
                    html_message=html_content
                )
                obj.email_sent=True
                obj.save()
