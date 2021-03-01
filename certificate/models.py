#models
from django.db import models
import uuid
from django.core.files import File
from events.models import Event
#signals
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from import_export.signals import post_import, post_export
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
    image_created = models.BooleanField(default=False,null=True)
    email_sent = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.name + " certificate for event " + self.event.title

@receiver(post_delete, sender=Certificate)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
