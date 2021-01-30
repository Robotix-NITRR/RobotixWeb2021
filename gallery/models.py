from django.db import models

# Create your models here.
class Gallery(models.Model):
    photo = models.ImageField(upload_to='img/gallery')
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.title
