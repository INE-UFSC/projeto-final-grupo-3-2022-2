import pygame
from abc import ABC

class BuildStructure(ABC, pygame.sprite.Sprite):
    def __init__(self, initial_position, width, height, image, fill=None):
        super(BuildStructure, self).__init__() # Inicia a classe ABC e a classe de Sprite
        
        self.__initial_position = initial_position
        if fill == None:
            self.__image = image
        else:
            self.__image = pygame.Surface((width, height))
            self.__image.fill(fill)
        self.__rect = self.__image.get_rect(topleft = initial_position)

    # Getters
    @property
    def image(self):
        return self.__image
    @property
    def rect(self):
        return self.__rect
    
    # Setters
    @image.setter
    def image(self, image: pygame.image):
        self.__image = image
        self.__rect = self.__image.get_rect(topleft = self.__initial_position)
