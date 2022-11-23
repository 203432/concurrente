import pygame
from tile import Tile
from player import Player
from enemy import Enemy
from settings import *
from debug import debug
from support import *
from random import choice
from weapon import *
from UI import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group() 

        self.current_attack = None
        self.create_map()

        self.ui = UI()

    def create_map(self):
        layouts = {
            'boundary':import_csv_layout('corte3/map/level_test_Bloqueo.csv'),
            'arbustos':import_csv_layout('corte3/map/level_test_Arbustos.csv'),
            'objetos':import_csv_layout('corte3/map/level_test_Objetos.csv'),
            'entidades':import_csv_layout('corte3/map/level_test_Entidades.csv')
        }
        graficos = {
            'arbusto': import_folder('corte3/graficos/arbustos'),
            'objeto': import_folder('corte3/graficos/objetos')
        }


        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'arbustos':
                            random_grass_image = choice(graficos['arbusto'])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
                        if style == 'objetos':
                            surf = graficos['objeto'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
                        if style == 'entidades':
                            if col =='394':
                                self.player = Player(
                                (x,y),
                                [self.visible_sprites],
                                self.obstacle_sprites,
                                self.create_attack,
                                self.destroy_attack,
                                self.create_magic)
                            else:
                                if col == '390': monster_name ='ghost'
                                elif col== '391': monster_name ='slime'
                                elif col=='392':monster_name = 'raccoon'
                                else: monster_name= 'squid'
                            enemy = Enemy(monster_name,(x,y),[self.visible_sprites],self.obstacle_sprites)
                            enemy.start()


    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])
    
    def create_magic(self,style,strength,cost):
        print(style)
        print(strength)
        print(cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]  // 2
        self.half_height = self.display_surface.get_size()[1]  // 2
        self.offset = pygame.math.Vector2()

        self.suelo_surf = pygame.image.load('corte3/images/map.png').convert()
        self.suelo_rect = self.suelo_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        floor_upset_pos = self.suelo_rect.topleft - self.offset
        self.display_surface.blit(self.suelo_surf,floor_upset_pos)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
    
    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)


# Better Call Saul es una serie de televisión estadounidense de drama creada por Vince Gilligan y Peter Gould, derivada 
# (spin-off) de Breaking Bad (2008-2013), también creada por Gilligan y de la que constituye a la vez una precuela y secuela.

# Ambientada entre principios y mediados de la década de 2000, la serie sigue la historia de Jimmy McGill 
# (interpretado por Bob Odenkirk), un estafador convertido en abogado y que posteriormente sería conocido como 
# Saul Goodman. La narración comienza seis años antes de los eventos de Breaking Bad y muestra la transformación 
# de McGill de ex-estafador de poca monta hasta convertirse en el abogado Saul Goodman, uno de los personajes principales 
# de Breaking Bad. La serie también explora parte del pasado de Mike Ehrmantraut (Jonathan Banks) y las circunstancias que 
# lo llevaron a convertirse tanto en la mano derecha del narcotráficante Gus Fring (Giancarlo Esposito) como en el detective´
# privado al que McGill usualmente recurre en Breaking Bad.