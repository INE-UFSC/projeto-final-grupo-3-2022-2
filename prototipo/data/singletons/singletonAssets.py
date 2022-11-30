import pygame
from os import path

import utility.finder as finder
from singletons.abstractSingleton import Singleton


class Assets(metaclass = Singleton):
    def load_assets(self):
        self.__fonts_path = {
            'title': finder.find_file('Fibberish.ttf'),
            'text': finder.find_file('PixelOperatorHB.ttf')
        }
        self.__images = {
            'background': pygame.image.load(finder.find_file('background.png')).convert_alpha(),
        }
        self.__level_images = {
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
            'gun': self.__get_image('gun.png', scale=3),
            'arrow': self.__get_image('arrow.png', scale=3)
        }
        self.__player = {
            'idle': [self.__get_image('idle.png', scale=3)],
            'run': [],
            'fall': []
        }

    def __get_image(self, image_name, scale = 1, search_in = path.join('prototipo', 'graphics')):
        image = pygame.image.load(finder.find_file(image_name, search_in)).convert_alpha()
        size = (image.get_width() * scale, image.get_height() * scale)
        return pygame.transform.scale(image, size)

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
    def user_name(self):
        try:
            return self.__user_name
        except:
            return '?'

    #Setters
    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name
