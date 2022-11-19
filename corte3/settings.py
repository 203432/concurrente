WIDTH = 1280
HEIGHT = 720
FPS = 30
TILESIZE = 64


BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'corte3/graficos/font/joystix.ttf'
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

weapon_data = {
    'sword':{'cooldown':100, 'damage':15, 'graphic': 'corte3/graficos/armas/sword/full.png'},
    'lance':{'cooldown':400, 'damage':30, 'graphic': 'corte3/graficos/armas/lance/full.png'},
    'axe':{'cooldown':300, 'damage':20, 'graphic': 'corte3/graficos/armas/axe/full.png'},
    'rapier':{'cooldown':50, 'damage':8, 'graphic': 'corte3/graficos/armas/rapier/full.png'},
    'sai':{'cooldown':80, 'damage':10, 'graphic': 'corte3/graficos/armas/sai/full.png'},
}

magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'corte3/graficos/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'corte3/graficos/particles/heal/heal.png'}
    }