from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Create your models here.
class ProductRegistration(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    summary = models.CharField(max_length=400)
    image = ProcessedImageField(
        upload_to="#",
        processors=[ResizeToFit(400,400)],
        format='JPEG',
        options={'quality':80}
    )
    detail = models.TextField()
    # options = 
    # option_price = 
    # location = 지도!!


class PhotographerProfile(models.Model):
    registration_date = models.DateTimeField('date registered')
    name = models.CharField(max_length=50)
    profile_photo = ProcessedImageField(
        upload_to="#",
        processors=[ResizeToFit(50,50)],
        format='JPEG',
        options={'quality':80}
    )
    introduction = models.TextField()
    portfolio = ProcessedImageField(
        upload_to="#",
        processors=[ResizeToFit(600,600)],
        format='JPEG',
        options={'quality':80}
    )
    # active_area = 지도!!
    camera = models.CharField(max_length=200)
    # reservations = 