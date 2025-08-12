from django.urls import path
from . import views
from .views import game_room

urlpatterns = [
    path('', views.home, name='home'),
    path('game_room/', game_room, name='game_room'),
    path('<str:room_name>/', views.game_room, name='room'),

]