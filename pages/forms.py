from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError
import re

#validate phone number according to the criterias given
def validate_phone(value):
    pattern = re.compile(r'^\+?1?\d{9,15}$') 
    if not pattern.match(value):
        raise ValidationError("Enter a valid phone number.")

class BasicUserForm(forms.ModelForm): 
    phone = forms.CharField(max_length=15, validators= [validate_phone])

    class meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email','phone','role']

class PatientRegistrationForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%y-%m-%d'],
        widget=forms.DateInput(format='%y-%m-%d')                           
        )
    class meta:
        model = CustomUser
        fiels = ['code','date_of_birth']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")



    
