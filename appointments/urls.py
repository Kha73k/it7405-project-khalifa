from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.services_list, name='services'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
]