import pygame
from os import path
from json import load

import utility.finder as finder
from singletons.abstractSingleton import Singleton


class Assets(metaclass = Singleton):
    def load_assets(self):
        self.__fonts_path = {
            'title': finder.find_file('Fibberish.ttf'),
            'text': finder.find_file('PixelOperatorHB.ttf')
        }
        self.__images = {
            'background': self.__get_image('background.png'),
        }
        self.__level_images = {
            'blocks': self.__load_sprite_sheet('block-sprite-sheet.png', 'block-sprite-sheet.json', scale = 3),
            'spike': self.__get_image('spike.png', 3),
            'target': [
                self.__get_image('target_001.png', 3),
                self.__get_image('target_002.png', 3),
            ],
            'door': [
                self.__get_image('door_001.png', scale=3),
                self.__get_image('door_002.png', scale=3),
                self.__get_image('door_003.png', scale=3),
                self.__get_image('door_004.png', scale=3),
            ],
            'gun': self.__get_image('crossbow.png', scale=3),
            'arrows': {
                'standart': self.__get_image('arrow-standart.png', scale=3),
                'bounce': self.__get_image('arrow-bounce.png', scale=3),
                'fast': self.__get_image('arrow-fast.png', scale=3),
                'piercing': self.__get_image('arrow-piercing.png', scale=3)
            }
        }
        self.__player = {
            'idle': [self.__get_image('idle.png', scale=3)],
            'run': [],
            'fall': []
        }
        self.__interface = {
            'arrows': {
                'standart': self.__get_image('arrow-icon-standart.png', scale=3),
                'bounce': self.__get_image('arrow-icon-bounce.png', scale=3),
                'fast': self.__get_image('arrow-icon-fast.png', scale=3),
                'piercing': self.__get_image('arrow-icon-piercing.png', scale=3)
            },
            'keys': {
                'wasd': self.__get_image('wasd.png', scale=3),
                'directions': self.__get_image('directions.png', scale=3),
                'esc': self.__get_image('esc.png', scale=3),
                'rmb': self.__get_image('rmb.png', scale=3),
                'lmb': self.__get_image('lmb.png', scale=3),
                'r': self.__get_image('r.png', scale=3)
            }
        }

    def __get_image(self, image_name, scale = 1, search_in = path.join('prototipo', 'graphics')):
        image = pygame.image.load(finder.find_file(image_name, search_in)).convert_alpha()
        size = (image.get_width() * scale, image.get_height() * scale)
        return pygame.transform.scale(image, size)

    def __load_sprite_sheet(self, sheet_image_name, sheet_json, scale = 1, search_in = path.join('prototipo', 'graphics')) -> dict:
        sheet_image = self.__get_image(sheet_image_name, scale, search_in = search_in)
        sheet_json_path = finder.find_file(sheet_json, search_in)
        with open(sheet_json_path, 'r') as json_file:
            sheet_data = load(json_file)
        
        quadrant_size = (sheet_data['quadrant_size'][0] * scale, sheet_data['quadrant_size'][1] * scale)
        sheet_images = {} # Dicionário que armazenará as imagens do sprite sheet e terá como chave os nomes
        for image_name, coord in sheet_data['coordinates'].items():
            image = pygame.Surface(quadrant_size)
            image.blit(sheet_image, (0, 0), (coord['x'] * quadrant_size[0], coord['y'] * quadrant_size[1], quadrant_size[0], quadrant_size[1]))
            sheet_images[image_name] = image
        
        return sheet_images

    # Getters
    @property
    def fonts_path(self):
        return self.__fonts_path
    @property
    def images(self):
        return self.__images
    @property
    def level_images(self):
        return self.__level_images
    @property
    def player(self):
        return self.__player
    @property
    def interface(self):
        return self.__interface
    
    @property
    def user_name(self):
        try:
            return self.__user_name
        except:
            return '?'

    #Setters
    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name
