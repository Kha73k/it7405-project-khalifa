from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'appointment_date', 'appointment_time', 'car_make', 'car_model', 'car_year', 'notes']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'car_make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Toyota'}),
            'car_model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Camry'}),
            'car_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2020'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any special requests?'}),
        }