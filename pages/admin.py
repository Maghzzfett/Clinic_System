from django.contrib import admin
from .models import Admin, Doctor, Patient, Appointment, Schedule, Persons

# Register your models here.
admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Schedule)