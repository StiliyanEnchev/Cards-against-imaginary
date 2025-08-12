from django.db import models

# Create your models here.

class GameRoom(models.Model):
    RoomName = models.CharField(unique=True, max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.RoomName

class Player(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    room = models.ForeignKey(GameRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name