import pygame

import utility.finder as finder
from singletons.abstractSingleton import Singleton


class Assets(Singleton):
    def __init__(self):
        super().__init__() # Inicia o Singleton

        self.load_assets()
    
    def load_assets(self):
        self.__fonts_path = {
            'title': finder.find_file('Fibberish.ttf'),
            'text': finder.find_file('PixelOperatorHB.ttf')
        }
        self.__images = {
            'background': pygame.image.load(finder.find_file('background.png')).convert_alpha(),
        }
        self.__level_images = {
            'spike': pygame.image.load(finder.find_file('spike.png')).convert_alpha(),
            'target': [
                pygame.image.load(finder.find_file('target_001.png')),
                pygame.image.load(finder.find_file('target_002.png'))
            ],
            'door': [
                pygame.image.load(finder.find_file('door_001.png')),
                pygame.image.load(finder.find_file('door_002.png')),
                pygame.image.load(finder.find_file('door_003.png')),
                pygame.image.load(finder.find_file('door_004.png'))
            ],
            'gun': pygame.image.load(finder.find_file('gun2.png')).convert_alpha(),
            'bow': [
                pygame.image.load(finder.find_file('bow_001.png')),
                pygame.image.load(finder.find_file('bow_002.png')),
                pygame.image.load(finder.find_file('bow_003.png')),
                pygame.image.load(finder.find_file('bow_004.png')),
                pygame.image.load(finder.find_file('bow_005.png')),
                pygame.image.load(finder.find_file('bow_006.png'))
            ],
            'player': pygame.image.load(finder.find_file('idle.png')).convert_alpha(),
        }

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
