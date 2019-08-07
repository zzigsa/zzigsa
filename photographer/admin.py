from django.contrib import admin
from .models import ProductRegistration
from .models import PhotographerProfile

# Register your models here.
admin.site.register(ProductRegistration)
admin.site.register(PhotographerProfile)