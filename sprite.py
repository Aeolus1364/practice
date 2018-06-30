import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Sprite, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.x_vel = 2

    def update(self, *args):
        self.rect.x += self.x_vel

