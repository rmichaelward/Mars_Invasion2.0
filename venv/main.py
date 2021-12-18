import pygame, sys, os

from button import Button
from levels import run_game
from settings_menu import change_settings
from high_scores import check_high_score

pygame.init()

#loading music/ playing it
pygame.mixer.music.load(os.path.join('music', 'instrumental1_16bit.wav'))
pygame.mixer.music.play()

clock = pygame.time.Clock()

def main_menu():
    click = False
    run = True
    WIDTH = 500
    HEIGHT = 531
    while run:
        pygame.display.set_caption("Mars Invasion")

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        bg = pygame.image.load(os.path.join('images', "main_menu_bg.png")).convert()

        new_game_button = Button(screen, 120, 230, 110, 50, "Start")
        high_scores_button = Button(screen, 280, 230, 110, 50, "Scores")
        settings_button = Button(screen, 120, 300, 110, 50, "Settings")
        quit_button = Button(screen, 280, 300, 110, 50, "Quit")


        screen.blit(bg, (0, 0))

        pos = pygame.mouse.get_pos()
        new_game_button.draw()
        high_scores_button.draw()
        settings_button.draw()
        quit_button.draw()

        if new_game_button.collides(pos):
            if click:
                run_game()

        if high_scores_button.collides(pos):
            if click:
                check_high_score()

        if settings_button.collides(pos):
            if click:
                change_settings()

        if quit_button.collides(pos):
            if click:
                pygame.quit()
                sys.exit()


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

main_menu()