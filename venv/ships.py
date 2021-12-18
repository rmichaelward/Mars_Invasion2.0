import pygame, os, json
from pygame.sprite import Sprite
import random

'''with open('player_sprite.json', "w") as file:
    sprite_choice = (('images', 'sprite_pack_1', 'PNG', 'playerShip1_red.png'))
    json.dump(sprite_choice, file)'''
'''with open('player_sprite.json', "r") as file:
    data = json.load(file)'''
'''with open('player_sprite.json', "r") as file:
    data1 = json.load(file)'''


class PlayerShip(Sprite):

    def __init__(self, screen):
        super().__init__()
        with open('player_sprite.json', "r") as file:
            data = json.load(file)
        if data == 'red1':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip1_red.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife1_red.png'))
        if data == 'red2':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip2_red.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife2_red.png'))
        if data == 'red3':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip3_red.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife3_red.png'))
        if data == 'blue1':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip1_blue.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife1_blue.png'))
        if data == 'blue2':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip2_blue.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife2_blue.png'))
        if data == 'blue3':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip3_blue.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife3_blue.png'))
        if data == 'orange1':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip1_orange.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife1_orange.png'))
        if data == 'orange2':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip2_orange.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife2_orange.png'))
        if data == 'orange3':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip3_orange.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife3_orange.png'))
        if data == 'green1':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip1_green.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife1_green.png'))
        if data == 'green2':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip2_green.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife2_green.png'))
        if data == 'green3':
            ship = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'playerShip3_green.png'))
            small_sprite = pygame.image.load(
                os.path.join('images', 'sprite_pack_1', 'PNG', 'UI', 'playerLife3_green.png'))

        self.image = ship
        self.life_sprite = small_sprite
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.center_vert = float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 5
        if self.moving_left and self.rect.left > 0:
            self.center -= 5
        if self.moving_up and self.rect.top > 0:
            self.center_vert -= 5
        if self.moving_down and self.rect.bottom < 700:
            self.center_vert += 5

        self.rect.centerx = self.center
        self.rect.centery = self.center_vert

    def draw(self):
        self.screen.blit(self.image, self.rect)
        #self.screen.blit(self.life_sprite, self.rect)

    def draw_lives(self):
        self.screen.blit(self.life_sprite, self.rect)


class Laser(Sprite):

    def __init__(self, screen, ship):
        super().__init__()

        laser_image = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'Lasers', 'laserRed01.png'))
        self.image = laser_image
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.speed = 6

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Enemy(Sprite):

    # Ideas: SOME ENEMIES CAN SHOOT LASERS BACK AT ME??

    def __init__(self, screen):
        super(Enemy, self).__init__()
        enemy_image = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'Enemies', 'enemyBlack1.png'))
        self.screen = screen
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(450 - self.rect.width)
        self.rect.y = -800
        self.speedy = random.randrange(3, 8)
        self.speedx = random.randrange(-3, 3)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top >= 750 or self.rect.right < -10 or self.rect.left > 600:
            self.rect.x = random.randrange(450 - self.rect.width)
            self.rect.y = random.randrange(-800, -80)
            self.speedy = random.randrange(3, 8)

    def blitenemy(self):
        self.screen.blit(self.image, self.rect)


class Enemy2(Enemy):

    def __init__(self, screen):
        enemy_image = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'Enemies', 'enemyBlack2.png'))
        super(Enemy, self).__init__()

        self.screen = screen
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.y = -800
        self.rect.x = random.randrange(450 - self.rect.width)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.health = 2
        self.speedy = random.randrange(2, 6)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        # NEED TO FIGURE OUT TIMER FOR LEFT RIGHT MOVEMENT OF ENEMY
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top >= 750 or self.rect.right < -10 or self.rect.left > 600:
            self.rect.x = random.randrange(450 - self.rect.width)
            self.rect.y = random.randrange(-800, -80)
            self.speedy = random.randrange(1, 6)


class Enemy3(Enemy):

    def __init__(self, screen):
        enemy_image = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'PNG', 'Enemies', 'enemyBlack3.png'))
        super(Enemy, self).__init__()

        self.screen = screen
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.y = -600
        self.rect.x = random.randrange(450 - self.rect.width)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.health = 3
        self.speedy = random.randrange(3, 7)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top >= 750 or self.rect.right < -10 or self.rect.left > 600:
            self.rect.x = random.randrange(450 - self.rect.width)
            self.rect.y = random.randrange(-800, -80)
            self.speedy = random.randrange(3, 7)
