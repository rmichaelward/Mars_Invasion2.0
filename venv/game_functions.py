import pygame, sys
import os
from ships import Laser, Enemy, Enemy2
from pygame.sprite import Group

lasers_group = Group()
enemy_group = Group()


def check_events(screen, ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ship)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, screen, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_laser(screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def fire_laser(screen, ship):
    new_laser = Laser(screen, ship)
    lasers_group.add(new_laser)


# THESE ADD ENEMIES TO GROUP< NEED TO DEFINE COLLISIONS AND DELETE THEM FROM SCREEN AND GROUP
# THEN SET UP LEVEL OF WHEN TO SPAWN AND HOW MANY TO SPAWN
def spawn_Enemy(screen):
    new_enemy = Enemy(screen)
    enemy_group.add(new_enemy)


def spawn_Enemy2(screen):
    new_enemy = Enemy2(screen)
    enemy_group.add(new_enemy)


def check_collisions(ship):
    global score
    laser_collide_enemy = pygame.sprite.groupcollide(lasers_group, enemy_group, True, True)
    hits = pygame.sprite.spritecollide(ship, enemy_group, False)
    if hits:
        sys.exit()
    #if laser_collide_enemy:
        print('collide')
        # Increase score
        #score += 1
        #print(score)


'''if laser_collide_enemy: #NOT WORKING BEACUE IT IS CHECKING FOR TRUE, BUT THIS RETURNS THE SPROTE??
        print("!")
    for laser in lasers_group.sprites():
        if pygame.sprite.spritecollide(laser, enemy_group, True, True):
            #explosion #NEED TO MAKE THIS WORK
            #lasers_group.remove(laser)
            #enemy_group.remove(enemy)
            kill(laser)
            print("LASER")

        if pygame.sprite.spritecollideany(ship, enemy_group):
            enemy_group.remove(enemy)
            #ADD LOSING A SHIP LIFE'''
