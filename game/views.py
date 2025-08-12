from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from game.forms import NickNameForm
from game.models import GameRoom, Player


# Create your views here.

def home(request):
    template_name = ('game.html')
    return render(request, template_name)

@csrf_exempt
def game_room(request, room_name=None):
    if request.method == "POST":
        # This POST can be either from username form or the initial join form
        username = request.POST.get("username")
        game_name = room_name or request.POST.get("game_name")

        if not game_name:
            return redirect('home')

        game_room, _ = GameRoom.objects.get_or_create(RoomName=game_name)
        player, _ = Player.objects.get_or_create(name=username, room=game_room)

        request.session['username'] = username
        request.session['game_name'] = game_name

        return redirect(reverse('room', kwargs={'room_name': game_name}))

    if room_name:
        username = request.session.get('username')

        if not username:
            return render(request, 'enter_username.html', {'room_name': room_name})

        game_room = get_object_or_404(GameRoom, RoomName=room_name)
        players = game_room.player_set.all()

        context = {
            'room_name': room_name,
            'username': username,
            'players': players,
        }
        return render(request, 'room.html', context)

    return redirect('home')

def game(request):
    template_name = ('game.html')
    return render(request, template_name)