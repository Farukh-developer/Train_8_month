from django.contrib import admin

# Register your models here.
from .models import Country_range, Servicetype, Availibilties, Text, Information

admin.site.register([Country_range, Servicetype, Availibilties, Text, Information])