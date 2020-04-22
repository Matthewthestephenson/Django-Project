from django.shortcuts import render

# Create your views here.
from home.models import Home

def home(request):
    projects = Home.objects.all()
    context = {
        'home': Home
    }
    return render(request, 'home.html', context)


