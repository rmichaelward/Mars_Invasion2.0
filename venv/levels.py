import pygame
import os, sys
from scoreboard import Scoreboard
from pygame.sprite import Group

from network.scores import ScoresModel
from ships import PlayerShip, Enemy, Enemy2, Enemy3
from game_functions import check_events, lasers_group, enemy_group, update_lasers


def run_game():
    W, H = 450, 700
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Mars Invasion')
    bg = pygame.image.load(os.path.join('images', "desert_big_looped.png")).convert()
    bgY = 0
    bgY2 = bg.get_height() * -1
    scoreboard = Scoreboard(screen)
    clock = pygame.time.Clock()

    #loading music/ playing it
    pygame.mixer.music.load(os.path.join('music', 'Battle_theme.wav'))
    pygame.mixer.music.play()

    ship = PlayerShip(screen)
    player_ships = Group()
    player_ships.add(ship)

    speed = 60

    for i in range(8):
        enemy1 = Enemy(screen)
        enemy2 = Enemy2(screen)
        enemy_group.add(enemy1)
        enemy_group.add(enemy2)

    run = True

    def redrawScreen():
        screen.blit(bg, (0, bgY))
        screen.blit(bg, (0, bgY2))

        scoreboard.show_score()
        update_lasers()
        hits = pygame.sprite.spritecollide(ship, enemy_group, False)
        if hits:
            for enemy in enemy_group:
                pygame.sprite.spritecollide(ship, enemy_group, True)
            scoreboard.ships_left -= 1

        # NEED TO UPDATE BELOW TO END THE GAME AND SEND HIGH SCORES
        if scoreboard.ships_left == 0:
            #assign game score to score
            score = scoreboard.save_score()
            print(score)
            print(type(score))
            #get user input on the name they want saved for leaderboard
            #Need to update this to make it in game, not in terminal
            username = input('What is your name')
            print(username)
            print(type(username))
            new_score = ScoresModel.save_score(username, score)
            #Show High Scores
            #Need to add a new screen to show scores
            top_scores = ScoresModel.get_scores()
            for dicts in top_scores:
                print('Player:', dicts['user'])
                print('Score:', dicts['score'])
            #Need to add a button on the screen for going back to the main menu
            from main import main_menu
            main_menu()

        # redraw enemies
        for enemy in enemy_group:
            enemy.update()
            enemy.blitenemy()

        # redraw player ship
        ship.update()
        ship.draw()

        # Check collisions of lasers and enemies, delete and update scoreboard
        for laser in lasers_group:
            num_enemy_collisions = 0
            if pygame.sprite.spritecollide(laser, enemy_group, False):
                num_enemy_collisions += 1
                scoreboard.score += 10 * num_enemy_collisions
            pygame.sprite.groupcollide(lasers_group, enemy_group, True, True)
        scoreboard.show_score()
        if scoreboard.score >= 150:
            run_level_two()

        pygame.display.update()

    def run_level_two():
        for enemy in enemy_group:
            enemy_group.remove(enemy)
        for laser in lasers_group:
            lasers_group.remove(laser)
        bg = pygame.image.load(os.path.join('images', 'sprite_pack_1', 'space_bg.png')).convert()
        bgY_lvl2 = 0
        bgY2_lvl2 = bg.get_height() * -1
        print('level2')
        run2 = True

        def redrawScreen2():
            screen.blit(bg, (0, bgY_lvl2))
            screen.blit(bg, (0, bgY2_lvl2))

            scoreboard.show_score()
            update_lasers()
            hits = pygame.sprite.spritecollide(ship, enemy_group, False)
            if hits:
                for enemy in enemy_group:
                    pygame.sprite.spritecollide(ship, enemy_group, True)
                scoreboard.ships_left -= 1

            # NEED TO UPDATE BELOW TO END THE GAME AND SEND HIGH SCORES
            if scoreboard.ships_left == 0:
                # assign game score to score
                score = scoreboard.save_score()
                print(score)
                print(type(score))
                # get user input on the name they want saved for leaderboard
                # Need to update this to make it in game, not in terminal
                username = input('What is your name')
                print(username)
                print(type(username))
                ScoresModel.save_score(username, score)
                # Show High Scores
                # Need to add a new screen to show scores
                ScoresModel.get_scores()
                # Need to add a button on the screen for going back to the main menu
                from main import main_menu
                main_menu()
            # redraw enemies
            for enemy in enemy_group:
                enemy.update()
                enemy.blitenemy()

            # redraw player ship
            ship.update()
            ship.draw()

            # Check collisions of lasers and enemies, delete and update scoreboard
            for laser in lasers_group:
                num_enemy_collisions = 0
                if pygame.sprite.spritecollide(laser, enemy_group, False):
                    num_enemy_collisions += 1
                    scoreboard.score += 10 * num_enemy_collisions
                pygame.sprite.groupcollide(lasers_group, enemy_group, True, True)
            scoreboard.show_score()
            if scoreboard.score >= 350:
                run_level_three()

            pygame.display.update()

        def run_level_three():
            for enemy in enemy_group:
                enemy_group.remove(enemy)
            for laser in lasers_group:
                lasers_group.remove(laser)
            bg = pygame.image.load(os.path.join('images', "earth_freeway.png")).convert()
            bgY_lvl3 = 0
            bgY2_lvl3 = bg.get_height() * -1
            print('level3')
            run3 = True

            def redrawScreen3():
                screen.blit(bg, (0, bgY_lvl3))
                screen.blit(bg, (0, bgY2_lvl3))

                scoreboard.show_score()
                update_lasers()
                hits = pygame.sprite.spritecollide(ship, enemy_group, False)
                if hits:
                    for enemy in enemy_group:
                        pygame.sprite.spritecollide(ship, enemy_group, True)
                    scoreboard.ships_left -= 1

                # NEED TO UPDATE BELOW TO END THE GAME AND SEND HIGH SCORES
                if scoreboard.ships_left == 0:
                    # assign game score to score
                    score = scoreboard.save_score()
                    print(score)
                    print(type(score))
                    # get user input on the name they want saved for leaderboard
                    # Need to update this to make it in game, not in terminal
                    username = input('What is your name')
                    print(username)
                    print(type(username))
                    ScoresModel.save_score(username, score)
                    # Show High Scores
                    # Need to add a new screen to show scores
                    ScoresModel.get_scores()
                    # Need to add a button on the screen for going back to the main menu
                    from main import main_menu
                    main_menu()
                # redraw enemies
                for enemy in enemy_group:
                    enemy.update()
                    enemy.blitenemy()

                # redraw player ship
                ship.update()
                ship.draw()

                # Check collisions of lasers and enemies, delete and update scoreboard
                for laser in lasers_group:
                    num_enemy_collisions = 0
                    if pygame.sprite.spritecollide(laser, enemy_group, False):
                        num_enemy_collisions += 1
                        scoreboard.score += 10 * num_enemy_collisions
                    pygame.sprite.groupcollide(lasers_group, enemy_group, True, True)
                scoreboard.show_score()
                if scoreboard.score >= 1000:
                    '''add_score(data)
                    data = {score: number, username: string}'''
                    #Add new screen fpor end game and a method on that screen for a user to input their name
                    #alternatively, have user input name before game starts? and have that track into this area
                    #the second idea might be hard to make work, not sure how to access that info in this file.
                    #maybe add a screen before the game starts where the user puts in their name
                    #their name is an attribute of an object and you can access that object anywhere in the program
                    top_scores = ScoresModel.save_score(username, Scoreboard.score)
                    #ADD END OF GAME

                pygame.display.update()

            while run3:
                bgY_lvl3 += 1.4
                bgY2_lvl3 += 1.4
                if bgY_lvl3 > bg.get_height():
                    bgY_lvl3 = bg.get_height() * -1
                if bgY2_lvl3 > bg.get_height():
                    bgY2_lvl3 = bg.get_height() * -1

                if len(enemy_group) < 8:
                    for i in range(12):
                        enemy1 = Enemy(screen)
                        enemy2 = Enemy2(screen)
                        enemy3 = Enemy3(screen)
                        enemy_group.add(enemy1, enemy2, enemy3)

                check_events(screen, ship)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run3 = False
                        pygame.quit()
                        quit()

                redrawScreen3()

                clock.tick(speed)

        while run2:
            bgY_lvl2 += 1.4
            bgY2_lvl2 += 1.4
            if bgY_lvl2 > bg.get_height():
                bgY_lvl2 = bg.get_height() * -1
            if bgY2_lvl2 > bg.get_height():
                bgY2_lvl2 = bg.get_height() * -1

            if len(enemy_group) < 7:
                for i in range(10):
                    enemy1 = Enemy(screen)
                    enemy2 = Enemy2(screen)
                    enemy3 = Enemy3(screen)
                    enemy_group.add(enemy1, enemy2, enemy3)

            check_events(screen, ship)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run2 = False
                    pygame.quit()
                    quit()

            redrawScreen2()

            clock.tick(speed)



    while run:
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
                enemy3 = Enemy3(screen)
                enemy_group.add(enemy1, enemy2, enemy3)

        check_events(screen, ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        redrawScreen()

        clock.tick(speed)
