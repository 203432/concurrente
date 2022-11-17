import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('corte3/images/idle_down.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)

        self.import_assets()
        self.status= 'down'
        self.frame_index =  0
        self.animation_speed = 0.15

        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.ataque = False
        self.cooldown = 400
        self.ataque_time = None

        self.obstacle_sprites = obstacle_sprites

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
            self.direction.x == 0 
            self.direction == 0
            if not 'attack' in self.status:
                if 'idle i self.status':
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
                print('atacandooooo')

            if keys[pygame.K_q]:
                self.ataque = True
                self.ataque_time = pygame.time.get_ticks()
                print('toma tu magia prro')

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x <0:
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y <0:
                        self.hitbox.top = sprite.hitbox.bottom


    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.ataque:
            if current_time - self.ataque_time >= self.cooldown:
                self.ataque = False

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
        