import pygame, sys

from ships import Laser
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
    if len(lasers_group) <= 3:
        new_laser = Laser(screen, ship)
        lasers_group.add(new_laser)


'''def check_collisions(ship):
    hits = pygame.sprite.spritecollide(ship, enemy_group, False)
    if hits:
        sys.exit()'''

def update_lasers():
    for laser in lasers_group:
        laser.update()
        laser.draw()
        # Check and delete lasers that leave the screen
        for laser in lasers_group:
            if laser.rect.bottom <= 0:
                lasers_group.remove(laser)