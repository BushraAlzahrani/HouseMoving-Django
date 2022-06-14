from django.contrib import admin
from .models import House, MovingTruck, Belongings, Appointment
# Register your models here.

admin.site.register(House)
admin.site.register(MovingTruck)
admin.site.register(Belongings)
admin.site.register(Appointment)

