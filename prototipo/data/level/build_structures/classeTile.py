import pygame
from level.build_structures.abstractBuildStructure import BuildStructure
from singletons.singletonAssets import Assets


class Tile(BuildStructure):
    def __init__(self, position, size, block_name = 'B_1'):
        SURFACE = Assets().level_images['blocks'][block_name.upper()]

        super().__init__(position, size, size, SURFACE)
