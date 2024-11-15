# class BasicUserForm(forms.ModelForm):
#     phone = forms.CharField(max_length=15, validators=[validate_phone])
    
#     class Meta:
#         model = CustomUser
#         fields = ['username','first_name','last_name', 'email', 'phone', 'gender', 'role']


# class PatientRegistrationForm(forms.ModelForm):
#     date_of_birth = forms.DateField(
#           input_formats=['%Y-%m-%d'],
#           widget=forms.DateInput(format='%Y-%m-%d')
#           )
    
#     class Meta:
#         model = CustomUser
#         fields = ['code', 'date_of_birth']

#     #perform additional form validation and processing using clean() method.
#     def clean(self):
#         cleaned_data = super().clean()
#         role = cleaned_data.get("role")# returns validated form fields in a dictionary format, according to role

#         if role != "Patient":
#             raise ValidationError("This form is only for Patients.")
        
#         if not cleaned_data.get("code"):
#             raise ValidationError("Code is required for Patients.")
        
#         if not cleaned_data.get("date_of_birth"):
#             raise ValidationError("Date of Birth is required for Patients.")

#         return cleaned_data

# class UserRegistrationForm(forms.ModelForm):
#     date_recorded = forms.DateTimeField(
#         input_formats=['%Y-%m-%d %H:%M:%S'],
#         widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S'),
#         required=False
#     )
    
#     class Meta:
#         model = CustomUser
#         fields = ['date_recorded','password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
    
#     #perform additional form validation involving multiple fields
#     def clean(self):
#         cleaned_data = super().clean()
#         role = cleaned_data.get("role")# returns validated form fields in a dictionary format, according to role

#         if role == "Admin" or role == "Doctor":
#             if not cleaned_data.get("date_recorded"):
#                 raise ValidationError("Date Recorded is required for Admin.")
#             if not cleaned_data.get("password"):
#                 raise ValidationError("Password is required for Admin.")
#         else:
#             raise ValidationError("This form is only for Admins and Doctors.")
        
#         return cleaned_data
    
# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['description', 'date_requested', 'approval_status', 'doctor', 'patient']

# class ScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Schedule
#         fields = ['date_scheduled', 'is_available', 'doctor']

# class MedicalRecordForm(forms.ModelForm):
#     class Meta:
#         model = MedicalRecord
#         fields = ['diagnosis', 'medical_history', 'test_result', 'date_update', 'patient', 'doctor']

# class TestForm(forms.ModelForm):
#     class Meta:
#         model = Test
#         fields = ['name', 'date_recorded', 'test_result', 'patient', 'medical_record']

# class PrescriptionForm(forms.ModelForm):
#     class Meta:
#         model = Prescription
#         fields = ['drug_type', 'drug_name', 'doctor', 'patient']
