import pygame
from level.build_structures.abstractBuildStructure import BuildStructure
from singletonAssets import Assets


class ExitDoor(BuildStructure):
    def __init__(self, position, block_size):
        IMAGE = Assets().level_images['door'][0]
        WIDTH = IMAGE.get_width()
        HEIGHT = IMAGE.get_height()

        # Como a imagem é mais alta que o tamanho usual do bloco, deve ser posicionada na região inferior do bloco
        POSITION = (position[0] + (block_size - WIDTH), position[1] + (block_size - HEIGHT))

        super().__init__(POSITION, WIDTH, HEIGHT, IMAGE)
        self.__unlocked = False

    def is_unlocked(self) -> bool:
        return self.__unlocked
    
    def unlock(self):
        self.__unlocked = True
        self.image = Assets().level_images['door'][-1]

    def collided(self, collided_with):
        return self.rect.colliderect(collided_with)
