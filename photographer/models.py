from django.db import models
from first.models import *
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

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
    options = models.CharField(max_length=500)
    option_price = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10000000),
            MinValueValidator(0)
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #location = models.CharField(max_length=300)
