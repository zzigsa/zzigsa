from django.contrib import admin
from first.models import User,Writer,EmailConfirm

admin.site.register(User)
admin.site.register(Writer)
admin.site.register(EmailConfirm)