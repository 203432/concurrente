import pygame
from settings import *
from support import *
from entity import *

class Player(Entity):
    def __init__(self,pos, groups, obstacle_sprites,create_attack,destroy_attack,create_magic):
        super().__init__(groups)
        self.image = pygame.image.load('corte3/images/idle_down.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.import_assets()
        self.status = 'down'

        self.ataque = False
        self.cooldown = 400
        self.ataque_time = None

        self.obstacle_sprites = obstacle_sprites

        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.cambiar_arma = True
        self.cambiar_arma_tiempo = None
        self.duracion_cambio = 200

        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        self.stats = {'salud':100,'estamina':60,'ataque':10,'mana':4,'velocidad':10}
        self.health = self.stats['salud'] * 0.5
        self.energy = self.stats['estamina']  * 0.8  
        self.exp = 123
        self.speed = self.stats['velocidad']


    def import_assets(self):
        path_assets = 'corte3/graficos/jugador/'
        self.animations ={
            'up':[],'down':[],'left':[],'right':[],'right_idle':[],'left_idle':[],'up_idle':[], 'down_idle':[],
            'right_attack':[], 'left_attack':[], 'up_attack':[], 'down_attack':[]
        }
        for animation in self.animations.keys():
            full_path = path_assets + animation
            self.animations[animation] =  import_folder(full_path)
            print(self.animations)

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        
        if self.ataque:
            self.direction.x = 0 
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def input(self):
        if not self.ataque:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            if keys[pygame.K_SPACE]:
                self.ataque = True
                self.ataque_time = pygame.time.get_ticks()
                self.create_attack()

            if keys[pygame.K_f]:
                self.ataque = True
                self.ataque_time = pygame.time.get_ticks()

                style = list(magic_data.keys())[self.magic_index]
                strength = list(magic_data.values())[self.magic_index]['strength'] + self.stats['mana']
                cost = list(magic_data.values())[self.magic_index]['cost']
                self.create_magic(style,strength,cost)

            if keys[pygame.K_q] and self.cambiar_arma:
                self.cambiar_arma = False
                self.cambiar_arma_tiempo = pygame.time.get_ticks()
                if self.weapon_index < len(list(weapon_data.keys()))-1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(weapon_data.keys())[self.weapon_index]

            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                if self.magic_index < len(list(magic_data.keys()))-1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.magic = list(magic_data.keys())[self.magic_index]
   

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.ataque:
            if current_time - self.ataque_time >= self.cooldown:
                self.ataque = False
                self.destroy_attack()

            if not self.cambiar_arma:
                if current_time - self.cambiar_arma_tiempo >= self.duracion_cambio:
                    self.cambiar_arma = True
            
            if not self.can_switch_magic:
                if current_time - self.magic_switch_time >= self.duracion_cambio:
                    self.can_switch_magic = True

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        