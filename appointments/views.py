from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Service, Appointment
from .forms import AppointmentForm

def services_list(request):
    services = Service.objects.all()
    return render(request, 'appointments/services.html', {'services': services})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('my_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book.html', {'form': form})

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    appointment.status = 'cancelled'
    appointment.save()
    messages.success(request, 'Appointment cancelled successfully.')
    return redirect('my_appointments')