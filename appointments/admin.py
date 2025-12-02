from django.contrib import admin
from .models import Service, Appointment

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'service', 'appointment_date', 'appointment_time', 'status']
    list_filter = ['status', 'appointment_date']