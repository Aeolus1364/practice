import pygame
import res
import cfg


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super(Sprite, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.x_vel = 0
        self.y_vel = 0

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel


class Player(Sprite):
    def __init__(self):
        super(Player, self).__init__(res.player)
        self.const_img = res.player
        self.direction = "right"
        self.past_coord = ()
        self.speed = 3

    def update(self):
        self.past_coord = self.rect.topleft
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        x_diff = self.rect.x - self.past_coord[0]
        y_diff = self.rect.y - self.past_coord[1]

        if x_diff > 0:
            self.direction = "right"
            self.image = pygame.transform.rotate(self.const_img, 270)
        elif x_diff < 0:
            self.direction = "left"
            self.image = pygame.transform.rotate(self.const_img, 90)
        elif y_diff > 0:
            self.direction = "down"
            self.image = pygame.transform.rotate(self.const_img, 180)
        elif y_diff < 0:
            self.direction = "up"
            self.image = self.const_img

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > cfg.dim[0]:
            self.rect.right = cfg.dim[0]
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > cfg.dim[1]:
            self.rect.bottom = cfg.dim[1]

    def draw(self, surface):
        surface.blit(self.image,self.rect)

class Projectile(Sprite):
    def __init__(self, dir, coord):
        super(Projectile,self).__init__(res.bee)
        self.direction = dir
        self.rect.center = coord
        self.speed = 4
        if self.direction == "up":
            self.y_vel -= self.speed
        elif self.direction == "down":
            self.y_vel += self.speed
            self.image = pygame.transform.rotate(res.bee, 180)
        elif self.direction == "left":
            self.x_vel -= self.speed
            self.image = pygame.transform.rotate(res.bee, 90)
        elif self.direction == "right":
            self.x_vel += self.speed
            self.image = pygame.transform.rotate(res.bee, 270)

    def update(self):
        if self.rect.left < 0:
            self.kill()
        elif self.rect.right > cfg.dim[0]:
            self.kill()
        elif self.rect.top < 0:
            self.kill()
        elif self.rect.bottom > cfg.dim[1]:
            self.kill()

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel






