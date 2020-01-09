from django.db import models
from random import randint, sample, choice
from time import sleep


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
        return str(randint(1, 21))

    enemy_list = ['Giant Scorpion Spider',
                  'Reaper',
                  'Ogre',
                  'Troll',
                  'Creeper',
                  'Witch',
                  'Red Dragon',
                  'Stone Beast',
                  'Warlock',
                  'Goblin']

    name = models.CharField(max_length=64)
    location = models.ForeignKey(Room,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    # enemy_type = models.CharField(max_length=64)
    HP = models.CharField(default=random_string)
    strength = models.CharField(default=random_string)

    def spawn_enemies(self):

        rooms = Room.objects.all()
        room_1 = choice(rooms)
        room_2 = choice(rooms)
        enemy_1 = choice(self.enemy_list)
        enemy_2 = choice(self.enemy_list)

        spawn_enemy1 = Enemy(name=enemy_1)
        spawn_enemy2 = Enemy(name=enemy_2)

        spawn_enemy1.save()
        spawn_enemy2.save()

        spawn_enemy1.location = room_1.id
        spawn_enemy2.location = room_2.id

        spawn_enemy1.save()
        spawn_enemy2.save()
            # spawned_enemies = sample(self.enemy_list, 2)
            # spawned_enemies[0] = choice(self.location)
            # spawned_enemies[1] = choice(self.location)

        #     return f'{self.name}, Beware of your enemies!, {self.location.room_name}'
        # else:
        #     return f'{self.name}, Are you afraid to fight?'

    def enemy_strikes_player(self, player):
        player_room = player.room
        enemy_in_room = Enemy.objects.filter(location=player_room)
        if len(enemy_in_room) > 0:
            sleep(5)
            player.HP = player.HP - enemy_in_room[0].strength
            player.save()
            return f'{player.name}, You have been hit and now your HP is {player.HP}'
        if player.HP <= 0:
            player.room = Room.objects.first().id
            player.save()
            return f'{player.name}, Oh no! You have been slain. Please try again from the beginning.'

    def player_strikes_enemy(self, player, enemy):
        player_room = player.room
        enemy_in_room = Enemy.objects.filter(location=player_room)
        if len(enemy_in_room) > 0:
            enemy.HP = enemy.HP - enemy_in_room[0].strength
            return f"{player.name}, You have hit {enemy.name} and now {enemy.name}'s is {enemy.HP}"
        if player.HP <= 0:
            player.room = Room.objects.first().id
            player.save()
            return f'{player.name}, Victory! You have slayed {enemy.name}!'

    def __str__(self):
        return f'{self.name} in {self.location}'
