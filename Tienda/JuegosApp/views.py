from django.shortcuts import redirect, render
from .models import Game

# Create your views here.
def home(request):
    games_list = Game.objects.all()
    return render(request, 'home/index.html', {'games': games_list})

def controlGame(request):
    games_list = Game.objects.all()
    return render(request, 'controlGame/control.html', {'games': games_list})

