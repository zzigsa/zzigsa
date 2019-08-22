from django.contrib import admin
from first.models import *

admin.site.register(User)
admin.site.register(Writer)
admin.site.register(EmailConfirm)
admin.site.register(Like)
admin.site.register(Reservation)