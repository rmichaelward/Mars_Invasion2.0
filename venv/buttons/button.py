import pygame


class Button:
    Blood_Red = (235, 0, 0)

    def __init__(self, screen, x, y, width, height, text="", color=(Blood_Red), hover=()):
        self.screen = screen
        self.clicked = False

        self.height = height
        self.width = width
        self.text = text
        self.color = color

        self.hover = (color[0] + 20, color[1] + 20, color[2] + 20)

        self.x = x
        self.y = y

        self.font = pygame.font.SysFont(None, 36)
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.topleft = (x, y)

    def collides(self, pos):
        return self.rect.collidepoint(pos)

    def draw(self):
        color = self.color
        if self.collides(pygame.mouse.get_pos()):
            color = self.hover
        pygame.draw.rect(self.screen, color, self.rect)

        if len(self.text):
            text_img = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text_img.get_rect(
                center=(self.rect.topleft[0] + (self.width // 2), self.rect.topleft[1] + (self.height // 2)))

            self.screen.blit(text_img, text_rect)


class SpriteButton:
    # Button for changing player sprites

    def __init__(self, position, image):
        self.position = position
        self.image = image

    def handle_event(self, event):
        "handle button getting clicked"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.position.collidepoint(event.position):
                print('pressed')
                # IF WORKS, ADD JSON FILE SAVE HERE FOR NEW SPRITE
    def collides(self, pos):
        return self.position.collidepoint(pos)

    def draw(self):
        self.screen.blit(self.image, self.position)
