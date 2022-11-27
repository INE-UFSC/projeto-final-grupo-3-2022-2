import pygame
from level.build_structures.abstractBuildStructure import BuildStructure
from singletonAssets import Assets


class Target(BuildStructure):
    def __init__(self, position):
        IMAGE = Assets().level_images['target']
        WIDTH = IMAGE.get_width()
        HEIGHT = IMAGE.get_height()

        super().__init__(position, WIDTH, HEIGHT, IMAGE)