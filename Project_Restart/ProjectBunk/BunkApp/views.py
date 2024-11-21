from django.shortcuts import render
from django.http import HttpResponse
from .models import Vote

def vote_view(request):
    results = None  # Initialize results variable

    if request.method == 'POST':
        vote_choice = request.POST.get('vote')
        if vote_choice:
            # Save the vote
            Vote.objects.create(vote_type=vote_choice)

            # Fetch the updated results
            results = {
                'yes': Vote.objects.filter(vote_type='yes').count(),
                'no': Vote.objects.filter(vote_type='no').count(),
            }

    # Render the form again, along with the results if they exist
    return render(request, 'BunkApp/index.html', {'results': results})
