from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.hashers import make_password, is_password_usable
# from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
# Create your models here.

from photographer.models import *

#유저
class User(AbstractUser):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    # check = models.BooleanField(default=False)    

    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)

    def __str__(self):
        return self.name    
    
#작가
class Writer(models.Model):

    userid = models.ForeignKey('User', on_delete=models.CASCADE,null=True, blank=True)
    introduce = models.TextField()
    profile_image = models.ImageField(upload_to="images/profile")
    camera = models.CharField(max_length=30)
    camera_image = models.ImageField(upload_to="image/camera")
    sns_email = models.TextField(blank=True)
    image = ProcessedImageField(
        upload_to="images/writer",
        processors=[ResizeToFit(50,50)],
        format='JPEG',
        options={'quality':80}
        )
    like = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.userid.name       


#좋아요
class Like(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    writerid = models.ForeignKey('Writer', on_delete=models.CASCADE,related_name='+',null=True, blank=True)


#예약상태
class Reservation(models.Model):
    userid = models.ForeignKey('User', on_delete=models.CASCADE)
    productid = models.ForeignKey('photographer.ProductRegistration', on_delete=models.CASCADE)
    progress = models.IntegerField()  # 0이면 예약대기 1이면 예약승인 2이면 구매이력에 추가


#이메일 전송
class EmailConfirm(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    key = models.CharField(max_length=60)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    @property
    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)