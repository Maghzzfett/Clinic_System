from typing import Any
from django.db import models

SPECIALIZATION_CHOICE = (
    ("Admin","Administrator"),
    ("Doctor","Docteor")
)

# Create your models here.
class Persons(models.Model):
    genderChoice= models.TextChoices("genderChoice", "male female")
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=genderChoice)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)
   
    class Meta:
        abstract = True

class Admin (Persons):
     specialization = models.CharField(max_length=200, choices= SPECIALIZATION_CHOICE)
     
     def __str__(self):
          return self.name
     
class DoctorType(models.Model):
     code_choice= models.TextChoices(
          "code_choice",
          "RAD MICRO BIOCHEM GASTRO")
     code= models.CharField(max_length=200, choices= code_choice, primary_key= True)
     proffession_choices= models.TextChoices(
          "proffession_choices",
            "Radiologist ClinicalMicrobiologist ClinicalBiochemist ClinicalGastroenterology")
     departmentChoises= models.TextChoices(
          "departmentChoises",
          "Radiology Gastroenterology ClinicalLaboratoryDepartment")
     proffession= models.CharField(max_length=200, choices= proffession_choices)
     department= models.CharField(max_length=200, choices= departmentChoises)
     

     def __str__(self):
          return self.profession

class Doctor (Persons):
     specialization = models.CharField(max_length=200, choices= SPECIALIZATION_CHOICE)
     is_active= models.BooleanField(default= True)
     admin = models.ForeignKey(Admin, on_delete= models.CASCADE)
     patient= models.ManyToManyField ("Patient", through= 'Appointment')
     doc_type= models.OneToOneField(DoctorType, on_delete=models.CASCADE)

     def __str__(self):
          return self.name

class Patient (Persons):
     date_recorded= models.DateTimeField()
     dateOf_birth=models.DateField()
     admin = models.ForeignKey(Admin, on_delete= models.CASCADE)

     def __str__ (self):
          return self.name
     
class Appointment(models.Model):
      description = models.TextField()
      date_requested = models.DateField()
      approval_status = models.BooleanField(default=False)
      admin = models.ForeignKey(Admin, on_delete= models.CASCADE)
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      
      def __str__(self):
           return f" {self.doctor} - {self.patient}"
      
class Schedule(models.Model):
      date_scheduled= models.DateTimeField()
      is_available= models.BooleanField(default= True)
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      admin = models.ForeignKey(Admin, on_delete= models.CASCADE)

      def __str__(self):
           return f"{self.date_scheduled}-{self.doctor}-{self.is_available}"
      
class MedicalRecord(models.Model):
     diagnosis= models.TextField(max_length=200)
     medicalHistory= models.TextField(max_length=300)
     testResult= models.TextField(max_length=200)
     dateUpdate= models.DateField()
     patient= models.ForeignKey(Patient, on_delete=models.CASCADE)
     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
     def __str__(self):
          return "%s 's Medical Record %s" % (self.patient)
     
class Test(models.Model):
     name= models.CharField(max_length=200)
     dateRecorded= models.DateField()
     testResult= models.TextField(max_length=200)
     patient= models.ForeignKey(Patient, on_delete=models.CASCADE)
     medicalRecord= models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
     

     def __str__ (self):
          return self.name

class Prescription(models.Model):
     drugType= models.CharField(max_length=200)
     drugName= models.CharField(max_length=200)
     doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE)
     patient= models.ForeignKey(Patient, on_delete=models.CASCADE)

     def __str__ (self):
          return f"{self.drugType}-{self.drugName}"