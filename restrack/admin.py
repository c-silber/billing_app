from django.contrib import admin

from .models import Facility, Residents

# Register your models here.
admin.site.register(Facility)
admin.site.register(Residents)