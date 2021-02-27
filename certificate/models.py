#models
from django.db import models
import uuid
from django.core.files import File
from events.models import Event
#signals
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
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


# Create your models here.
class Certificate(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url_key = models.UUIDField(default=uuid.uuid4,unique=True, blank=True,  null=True)
    image = models.ImageField(upload_to='certificate/',null=True,blank=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name + " certificate for event " + self.event.title



@receiver(post_save,sender=Certificate)
def img_handler(created,instance,*args,**kwargs):
    if created:
        image_url = "https://robotix.nitrr.ac.in/static/img/cert.jpg"
        #font_url = "http://127.0.0.1:8000/static/font/Raleway-Regular.ttf"
        response = requests.get(image_url, stream=True)
        if response.status_code != requests.codes.ok:
            print("error")
            instance.save()
        else:
            file_name = image_url.split('/')[-1]
            # print(file_name)
        
            # Create a temporary file
            lf = tempfile.NamedTemporaryFile()

            # Read the streamed image in sections
            for block in response.iter_content(1024 * 8):
                
                # If no more file then stop
                if not block:
                    break

                # Write image block to temporary file
                lf.write(block)
            my_img = Image.open(lf)
            d1 = ImageDraw.Draw(my_img)
            name = str(instance.name)
            event_name = str(instance.event.title)
            d1.text((460, 410), name,  fill="black")
            d1.text((400, 270), event_name,  fill="black")
            new_img_temp_file = tempfile.NamedTemporaryFile(suffix = '.jpeg')
            my_img.save(new_img_temp_file)

            instance.image.save(file_name, files.File(new_img_temp_file))
            instance.save()

            html_content = '<h3>This is an sample yet <strong>important</strong> message to all the participants.</h3>'
            msg = EmailMultiAlternatives(
                'Get your certificate',               # subject,
                'Download this certificate here!',      # text_content,
                '{}'.format(settings.EMAIL_HOST_USER),                # from_email,
                ['{}'.format(instance.email),],             # to email(s)
            )
            msg.attach_alternative(html_content, "text/html")
            msg.attach_file('media/{}'.format(instance.image))
            msg.send()


@receiver(post_delete, sender=Certificate)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

