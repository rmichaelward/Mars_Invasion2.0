import pygame
import os
from pygame.sprite import Group
from ships import PlayerShip, Laser, Enemy, Enemy2
from game_functions import check_events, lasers_group, enemy_group, check_collisions, spawn_Enemy, spawn_Enemy2


def run_game():
    W, H = 450, 700
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Mars Invasion')

    bg = pygame.image.load(os.path.join('images', "desert_big_looped.png")).convert()
    bgY = 0
    bgY2 = bg.get_height() * -1

    #score = 0
    clock = pygame.time.Clock()

    # also possibly need to run 3 different levels with the level spawn enemy events being separate form the screen redraw?
    def redrawScreen():
        #largeFont = pygame.font.SysFont('Moondance', 30)
        #text = largeFont.render('Score: ' + str(score), 1, (255,255,255))
        screen.blit(bg, (0, bgY))
        screen.blit(bg, (0, bgY2))
        #screen.blit(text, (700, 10))

        # fire lasers from group
        for laser in lasers_group:
            laser.update()
            laser.draw()
            # Check and delete lasers that leave the screen
            for laser in lasers_group:
                if laser.rect.bottom <= 0:
                    lasers_group.remove(laser)
        check_collisions(ship)
        # redraw enemies
        for enemy in enemy_group:
            enemy.update()
            enemy.blitenemy()
        # USED TO MAKE SURE ABOVE IS WORKING print(len(enemy_group))

        # redraw player ship
        ship.update()
        ship.draw()
        check_collisions(ship)

        pygame.display.update()

    ship = PlayerShip(screen)
    # BELOW METHOD DID NOT WORK. TO BE REMOVED
    # enemy = Enemy(screen)
    # enemy2 = Enemy2(screen)
    # spawned = pygame.USEREVENT
    # spawned2 = pygame.USEREVENT + 1
    # pygame.time.set_timer(spawned, 2000)
    # pygame.time.set_timer(spawned2, 3000)

    speed = 60

    for i in range(8):
        enemy1 = Enemy(screen)
        enemy2 = Enemy2(screen)
        enemy_group.add(enemy1)
        enemy_group.add(enemy2)

    run = True

    while run:
        ##THIS LOOP WILL SCROLL BG. NEED TO DESIGN LEVELS AND USE THIS LOOP TO MOVE THE BG
        bgY += 1.4
        bgY2 += 1.4
        if bgY > bg.get_height():
            bgY = bg.get_height() * -1
        if bgY2 > bg.get_height():
            bgY2 = bg.get_height() * -1

        if len(enemy_group) < 5:
            for i in range(8):
                enemy1 = Enemy(screen)
                enemy2 = Enemy2(screen)
                enemy_group.add(enemy1)
                enemy_group.add(enemy2)

        check_events(screen, ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        redrawScreen()

        clock.tick(speed)
