from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Destination)
admin.site.register(models.Travel_courses)
admin.site.register(models.Tourism_courses)
admin.site.register(models.Hospitality_courses)
admin.site.register(models.Hotel)
admin.site.register(models.UserDestinations)
