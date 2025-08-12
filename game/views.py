from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from game.forms import NickNameForm


# Create your views here.

def home(request):
    template_name = ('game.html')
    return render(request, template_name)

@csrf_exempt
def game_room(request, room_name=None):
    if request.method == "POST":
        game_name = request.POST.get("game_name")
        username = request.POST.get("username")

        print(f"Game: {game_name}, User: {username}")
        return redirect(reverse('room', kwargs={'room_name': game_name}))

    return render(request, 'room.html')

def game(request):
    template_name = ('game.html')
    return render(request, template_name)