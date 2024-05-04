from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Review

# Create your views here.

def review(request):
    
    if request.method == "POST":
        full_name = request.POST['full-name']
        movie = request.POST['movie']
        review = request.POST['review']
        
        if full_name and movie and review:
        
            create_review = Review.objects.create(
                full_name = full_name,
                movie=movie,
                user_review = review
            )
            
            create_review.save()
        
        else:
            return HttpResponse("Please enter all the values!")
        
        return HttpResponseRedirect('/all-reviews')
    
    return render(request, 'reviews/review.html')

def thank_you(request):
            
    all_reviews = Review.objects.all()
    
    return render(request, 'reviews/all-reviews.html', {
        'reviews' : all_reviews,
    })