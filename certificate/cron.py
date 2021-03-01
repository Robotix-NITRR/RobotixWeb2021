from .models import Certificate
#emalis
from django.core.mail import send_mail
from django.conf import settings
#PIL
from PIL import Image, ImageDraw,ImageFont
#utill
import requests
import tempfile
from django.core import files
import os
from io import BytesIO

def cert_job():
    objs = Certificate.objects.all().filter(image_created=False)
    image_url = "https://robotix.nitrr.ac.in/static/img/certificate/Roboquiz2/pcert.jpeg"
    req = requests.get("https://robotix.nitrr.ac.in/static/fonts/Satisfy-Regular.ttf?raw=true")
    idfont = requests.get("https://robotix.nitrr.ac.in/static/fonts/Montserrat-Regular.ttf?raw=true")
    
    image_font = ImageFont.truetype(BytesIO(req.content), 130)
    id_font = ImageFont.truetype(BytesIO(idfont.content), 80)
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
            key = str(obj.url_key)
            if len(name.split(" ")) == 1:
                d1.text((2470, 1610), name,font=image_font,  fill="black")
            else:
                d1.text((2270, 1610), name,font=image_font,  fill="black")

            d1.text((3530, 3270), key, font=id_font, fill="#000000")

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
                html_content='<p>It was absolutely wonderful to have you participate in the Roboquiz 2.0. Thankyou for showing us your support and belief.</p><p>Our journey together has just started and as a first step, here’s wishing you…Congratulations!</p><br><br><p>For being spirited and driven. For believing in yourself. For your courage to compete with students and professionals all over India and abroad. For giving it your best shot.</p><p>There are many opportunities that we will soon be sending your way to take your knowledge quotient a notch higher!</p><br><br><p>All you need to do is stay in touch with us at:</p><p>Instagram: https://www.instagram.com/robotix_nitrr/</p><p>Facebook: https://m.facebook.com/nitrrobots16/</p><p>Website: http://www.robotix.nitrr.ac.in/</p><p>Email: robotixclub@nitrr.ac.in</p><p>Wishing you the best!</p><br><img style="height:400px;width:600px" src="https://robotix.nitrr.ac.in{0}" alt="Your Certificate"><br><p>Your unique certificate id is : <strong>{1}</strong> </p><p>ROBOTiX Club</p><p><strong>NIT Raipur</strong></p><p><i>To verify and download this certificate <a href="https://robotix.nitrr.ac.in/certificate/{2}">click here </a><i> </p>'.format(obj.image.url,obj.url_key,obj.url_key)
                send_mail(
                    'Certificate for {}'.format(obj.event.title),
                    '',
                    'wandavision5432@gmail.com',
                    ['{}'.format(obj.email)],
                    fail_silently=False,
                    html_message=html_content
                )
                obj.email_sent=True
                obj.save()
