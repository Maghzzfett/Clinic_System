from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,Group,Permission


USER_ROLES= [
     ('Admin','Admin'),
     ('Doctor', 'Doctor'), 

     ('Patient', 'Patient'),
]

GENDER= [
     ('MALE','male'),
     ('FEMALE','female'),
]

# Create your models here.
class CustomUser(AbstractUser):
    role = models.CharField(max_length=30, choices=USER_ROLES)
    gender = models.CharField(max_length=10, choices=GENDER)
    phone = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
    date_recorded = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField()
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')

    def __str__(self):
        return f"{self.username} - {self.role}"
    

class Appointment(models.Model):
    description = models.TextField()
    date_requested = models.DateField()
    approval_status = models.BooleanField(default=False)
    doctor = models.ForeignKey(CustomUser, limit_choices_to={'role': 'DOCTOR'}, related_name='doctor_appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(CustomUser, limit_choices_to={'role': 'PATIENT'}, related_name='patient_appointments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor.username} - {self.patient.username}"

class Schedule(models.Model):
    date_scheduled = models.DateTimeField()
    is_available = models.BooleanField(default=True)
    doctor = models.ForeignKey(CustomUser, limit_choices_to={'role': 'DOCTOR'}, related_name='doctor_schedules', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_scheduled} - {self.doctor.username} - {self.is_available}"

class MedicalRecord(models.Model):
    diagnosis = models.TextField()
    medical_history = models.TextField()
    test_result = models.TextField()
    date_update = models.DateField()
    patient = models.ForeignKey(CustomUser, limit_choices_to={'role': 'PATIENT'}, related_name='patient_medical_records', on_delete=models.CASCADE)
    doctor = models.ForeignKey(CustomUser, limit_choices_to={'role': 'DOCTOR'}, related_name='doctor_medical_records', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.username}'s Medical Record"

class Test(models.Model):
    name = models.CharField(max_length=50)
    date_recorded = models.DateField()
    test_result = models.TextField()
    patient = models.ForeignKey(CustomUser, limit_choices_to={'role': 'PATIENT'}, related_name='patient_tests', on_delete=models.CASCADE)
    medical_record = models.ForeignKey(MedicalRecord, related_name='medical_record_tests', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    drug_type = models.CharField(max_length=50)
    drug_name = models.CharField(max_length=50)
    doctor = models.ForeignKey(CustomUser, limit_choices_to={'role': 'DOCTOR'}, related_name='doctor_prescriptions', on_delete=models.CASCADE)
    patient = models.ForeignKey(CustomUser, limit_choices_to={'role': 'PATIENT'}, related_name='patient_prescriptions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.drug_type} - {self.drug_name}"