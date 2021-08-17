from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio



def index(request):

    home = Home.objects.latest('updated')
    context = {
        'home': home,
    }

    return render(request, 'index.html', context)
# Create your views here.
