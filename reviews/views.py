from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

def reviews_list(request):
    try:
        all_reviews = list(Review.objects.all())
        reviews = [r for r in all_reviews if r.is_approved == True]
    except:
        reviews = []
    
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Thank you! Your review has been submitted and is awaiting approval.')
            return redirect('reviews_list')
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/add_review.html', {'form': form})