import pygame
import var

pygame.init()


class Guy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.BROWN)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.xspeed = -8
        if keystate[pygame.K_d]:
            self.xspeed = 8
        if keystate[pygame.K_w]:
            self.yspeed = -8
        if keystate[pygame.K_s]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1
