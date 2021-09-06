import pygame
import var
import random
pygame.init()
pygame.mixer.init()


class RoamPichu(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.transform.scale(pichu_img, (20, 20))
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.YELLOW)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)

        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        self.wander = True

    def update(self):
        if self.wander:
            self.rect.centerx += (random.randint(1, 10))
            self.rect.centerx -= (random.randint(1, 10))
            self.rect.centery += (random.randint(1, 10))
            self.rect.centery -= (random.randint(1, 10))
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1



