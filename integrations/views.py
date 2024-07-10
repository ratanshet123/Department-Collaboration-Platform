from django.shortcuts import render

def integrations_view(request):
    return render(request, 'integrations/integrations.html')
