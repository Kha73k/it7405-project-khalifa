from django.shortcuts import render
from reviews.models import Review
from appointments.models import Service

def home(request):
    try:
        all_reviews = list(Review.objects.all().order_by('-created_at'))
        reviews = [r for r in all_reviews if r.is_approved == 1][:3]
    except:
        reviews = []
    
    return render(request, 'home.html', {'reviews': reviews})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})