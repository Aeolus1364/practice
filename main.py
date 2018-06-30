import pygame
import sprite
import res


class Main:
    def __init__(self):
        pygame.init()
        self.surf = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.running = True
        self.sprite = sprite.Sprite(res.planet2)
        self.group = pygame.sprite.Group(self.sprite)
        self.group.add(sprite.Sprite(res.planet2))

    def main_loop(self):
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.surf.fill((255, 255, 255))

            self.group.draw(self.surf)
            self.group.update()

            pygame.display.update()

            self.clock.tick(self.fps)
            
        pygame.quit()


main = Main()
main.main_loop()
