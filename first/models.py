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
#유저
class User(AbstractUser):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    # check = models.BooleanField(default=False)    
    writer = models.OneToOneField('Writer', on_delete=models.CASCADE, related_name='user_writer', blank=True, null=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
#작가
class Writer(models.Model):
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
    like_user_set = models.ManyToManyField('User', blank=True, related_name='like_user_set', through='Like')

    @property
    def like_count(self):
        return self.like_user_set.count()

#좋아요
class Like(models.Model):
    username = models.ForeignKey('User', on_delete=models.CASCADE)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

#이메일 전송
class EmailConfirm(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    key = models.CharField(max_length=60)
    is_confirmed = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
        