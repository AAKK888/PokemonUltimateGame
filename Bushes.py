import random
import pygame
import var

pygame.init()
pygame.mixer.init()


class BushesAndStuff(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((random.randint(30, 50), random.randint(30, 50)))
        self.image.fill(var.GREEN)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, var.WIDTH), (random.randint(0, var.HEIGHT)))

    def update(self):
        pass
