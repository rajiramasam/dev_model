from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nurse_first_name', 'nurse_last_name',  'patient_first_name', 'patient_last_name','health_issue', 'response_to_medication']
        widgets = {
            'health_issue': forms.Textarea(attrs={'rows': 4}),
            'response_to_medication': forms.Textarea(attrs={'rows': 4}),
        }
