import pygame
import sprite
import res
import cfg


class Main:
    def __init__(self):
        pygame.init()
        self.surf = pygame.display.set_mode(cfg.dim)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.player = sprite.Player()
        self.bees = pygame.sprite.Group()

    def main_loop(self):
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.y_vel -= self.player.speed
                        self.player.x_vel = 0
                    if event.key == pygame.K_DOWN:
                        self.player.y_vel += self.player.speed
                        self.player.x_vel = 0
                    if event.key == pygame.K_LEFT:
                        self.player.y_vel = 0
                        self.player.x_vel -= self.player.speed
                    if event.key == pygame.K_RIGHT:
                        self.player.x_vel += self.player.speed
                        self.player.y_vel = 0
                    if event.key == pygame.K_SPACE:
                        self.bees.add(sprite.Projectile(self.player.direction, self.player.rect.center))


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        if self.player.y_vel:
                            self.player.y_vel += self.player.speed
                    if event.key == pygame.K_DOWN:
                        if self.player.y_vel:
                            self.player.y_vel -= self.player.speed
                    if event.key == pygame.K_LEFT:
                        if self.player.x_vel:
                            self.player.x_vel += self.player.speed
                    if event.key == pygame.K_RIGHT:
                        if self.player.x_vel:
                            self.player.x_vel -= self.player.speed

            self.surf.fill((255, 255, 255))


            self.bees.update()
            self.player.update()
            self.bees.draw(self.surf)
            self.player.draw(self.surf)




            pygame.display.update()

            self.clock.tick(self.fps)
            
        pygame.quit()


main = Main()
main.main_loop()
