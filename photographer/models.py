from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.core.validators import MaxValueValidator, MinValueValidator
from first.models import *

# 상품 등록
class ProductRegistration(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=400)
    image = ProcessedImageField(
        upload_to="images/product",
        processors=[ResizeToFit(400,400)],
        format='JPEG',
        options={'quality':80}
    )
    detail = models.TextField()
    options = models.CharField(max_length=400)
    option_price = models.IntegerField()  
   
    writerid = models.ForeignKey('first.Writer', on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.title    
 
 #댓글
class Reply(models.Model):
    productid = models.ForeignKey('ProductRegistration', on_delete=models.CASCADE)
    writer = models.CharField(max_length=20)
    content = models.CharField(max_length=400)
    rating = models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)
    
# #옵션
# class Option(models.Model):
#     productid = models.ForeignKey('ProductRegistration', on_delete=models.CASCADE)
#     content = models.CharField(max_length=400)
#     price = models.IntegerField()  