from django.db import models


# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to='static/img_gallery/')
    name = models.CharField(max_length=200)