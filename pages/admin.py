from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Admin)
admin.site.register(Doctor)
admin.site.register(DoctorType)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Schedule)
admin.site.register(MedicalRecord)
admin.site.register(Test)
admin.site.register(Prescription)
