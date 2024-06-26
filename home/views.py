from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home/home.html')
def search_results(request):
    query = request.GET.get('query', '')
    context = {
        'query': query,
    }
    return render(request, 'home/search_results.html', context)