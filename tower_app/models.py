from django.db import models
from random import randint


class Room(models.Model):
    room_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.room_name}"


class Player(models.Model):
    name = models.CharField(max_length=64)
    location = models.ForeignKey(Room,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)

    def move(self):
        pass

    def __str__(self):
        return f"{self.name} in {self.location}"


class Enemy(models.Model):

    def random_string(self):
        return str(randint(0,5))

    name = models.CharField(max_lenght=64)
    location = models.ForeignKey(Room,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    enemy_type = models.CharField(max_length=64)
    hp = models.CharField(default=random_string)
    defense_strength = models.CharField(default=random_string)

    def strike(self):
        pass

    def perish(self):
        pass

    def __str__(self):
        return f'{self.name} in {self.location}'
