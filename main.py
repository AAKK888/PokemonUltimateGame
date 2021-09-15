# import random
import time
import pygame
import var
from AllPokemon import *
from Guy import *

screen = pygame.display.set_mode((var.WIDTH, var.HEIGHT))

from Bushes import *
from RoamingPokemon import *

img_dir = path.join(path.dirname(__file__), 'img')
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Pokemon Game ")
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, "BackroundGrassyPlains.png")).convert()
goodback = pygame.transform.scale(background, (var.WIDTH, var.HEIGHT))
background_rect = goodback.get_rect()
screen.fill(var.BLUE)

font_name = pygame.font.match_font('arial')


def draw_text(text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, var.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


all_sprites = pygame.sprite.Group()
pokemongroup = pygame.sprite.Group()
bushesgroup = pygame.sprite.Group()
wildpokemongroup = pygame.sprite.Group()

Bush = BushesAndStuff()
# all_sprites.add(Bush)
bushesgroup.add(Bush)
Bush2 = BushesAndStuff()
# all_sprites.add(Bush2)
bushesgroup.add(Bush2)
Bush3 = BushesAndStuff()
# all_sprites.add(Bush3)
bushesgroup.add(Bush3)
Bush4 = BushesAndStuff()
# all_sprites.add(Bush4)
bushesgroup.add(Bush4)
Bush5 = BushesAndStuff()
# all_sprites.add(Bush5)
bushesgroup.add(Bush5)
Bush6 = BushesAndStuff()
# all_sprites.add(Bush6)
bushesgroup.add(Bush6)
Bush7 = BushesAndStuff()
# all_sprites.add(Bush7)
bushesgroup.add(Bush7)
Bush8 = BushesAndStuff()
# all_sprites.add(Bush8)
bushesgroup.add(Bush8)
Bush9 = BushesAndStuff()
# all_sprites.add(Bush9)
bushesgroup.add(Bush9)
Bush10 = BushesAndStuff()
# all_sprites.add(Bush10)
bushesgroup.add(Bush10)
Bush11 = BushesAndStuff()
# all_sprites.add(Bush11)
bushesgroup.add(Bush11)
Bush12 = BushesAndStuff()
# all_sprites.add(Bush12)
bushesgroup.add(Bush12)
Bush13 = BushesAndStuff()
# all_sprites.add(Bush13)
bushesgroup.add(Bush13)
Bush14 = BushesAndStuff()
# all_sprites.add(Bush14)
bushesgroup.add(Bush14)
Bush15 = BushesAndStuff()
# all_sprites.add(Bush15)
bushesgroup.add(Bush15)

MyCharac = Guy()
all_sprites.add(MyCharac)

Pikachu = PichuEvo(5)
pokemongroup.add(Pikachu)
Wild_Pichu = RoamPichu(5)
wildpokemongroup.add(Wild_Pichu)

running = True
SeeWhoIsPokemon = 1
currentPokemon = 'pikachu'
while running:
    #                   check events
    clock.tick(var.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                if SeeWhoIsPokemon == 0:
                    pokemongroup.remove(Onix)
                    Pikachu2 = PichuEvo(5)
                    pokemongroup.add(Pikachu2)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Pikachu.name
                else:
                    pass
                if SeeWhoIsPokemon == 1:
                    pokemongroup.remove(Pikachu)
                    Bulbasaur = BulbasaurEvo(5)
                    pokemongroup.add(Bulbasaur)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Bulbasaur.name
                else:
                    pass
                if SeeWhoIsPokemon == 2:
                    pokemongroup.remove(Bulbasaur)
                    Charmander = CharmanderEvo(5)
                    pokemongroup.add(Charmander)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Charmander.name
                else:
                    pass
                if SeeWhoIsPokemon == 3:
                    pokemongroup.remove(Charmander)
                    Squirtle = SquirtleEvo(5)
                    pokemongroup.add(Squirtle)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Squirtle.name
                else:
                    pass
                if SeeWhoIsPokemon == 4:
                    pokemongroup.remove(Squirtle)
                    Onix = OnixEvo(5)
                    pokemongroup.add(Onix)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Squirtle.name
                else:
                    pass
                if SeeWhoIsPokemon == 5:
                    pokemongroup.remove(Onix)
                    Fletchling = FletchlingEvo(5)
                    pokemongroup.add(Fletchling)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Fletchling.name
                else:
                    pass
                if SeeWhoIsPokemon == 6:
                    pokemongroup.remove(Fletchling)
                    Magikarp = MagikarpEvo(5)
                    pokemongroup.add(Magikarp)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Magikarp.name
                else:
                    pass
                if SeeWhoIsPokemon == 7:
                    pokemongroup.remove(Magikarp)
                    Farfetch_d = Farfetch_dEvo(5)
                    pokemongroup.add(Farfetch_d)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Farfetch_d.name
                else:
                    pass
                if SeeWhoIsPokemon == 8:
                    pokemongroup.remove(Farfetch_d)
                    Elekid = ElekidEvo(5)
                    pokemongroup.add(Elekid)
                    SeeWhoIsPokemon += 1
                    currentPokemon = Elekid.name
                else:
                    pass
                if SeeWhoIsPokemon == 9:
                    pokemongroup.remove(Elekid)
                    Gastly = GastlyEvo(5)
                    pokemongroup.add(Gastly)
                    SeeWhoIsPokemon = 0
                    currentPokemon = Gastly.name
                else:
                    pass
            elif event.type == pygame.K_SPACE:
                Pikachu.domove()

    hits = pygame.sprite.spritecollide(MyCharac, pokemongroup, False)
    if hits:
        MyCharac.rect.x += 10
        MyCharac.rect.y += 10

    # 2. Update
    all_sprites.update()
    pokemongroup.update()
    bushesgroup.update()
    wildpokemongroup.update()
    movegroup.update()

    # 3. Draw / render
    screen.fill(var.BLACK)
    screen.blit(goodback, background_rect)

    all_sprites.draw(screen)
    pokemongroup.draw(screen)
    bushesgroup.draw(screen)

    # after drawing everything, flip the display
    pygame.display.flip()
    time.sleep(0.001)

pygame.quit()
