from django.contrib import admin

from .models import Journey, Car, Driver, Ride, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Journey)
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Ride)
