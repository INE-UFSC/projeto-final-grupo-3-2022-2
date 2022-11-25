import pygame
from states.abstractState import State
from states.classeButton import Button
from singletonAssets import Assets
from Settings import Settings
from level.classeLevel import Level
import config

from states.stateLevelPaused import LevelPaused


class LevelPlaying(State):
    def __init__(self, game):
        super().__init__(game)

        self.__assets = Assets()
        self.__background = self.__assets.images['background']
        self.__buttons = pygame.sprite.Group()
        
        self.__load_level(0)
        
    def __load_level(self, level_selected):
        current_level = config.levels[level_selected]
        self.level = Level(current_level) # Passa a matriz que representa o nível e a superfície onde o nível será desenhado


    def update(self, delta_time, actions):
        # Se o jogador pressionar ESC, entra no estado de pausa
        if actions['esc']:
            pause_state = LevelPaused(self._game)
            pause_state.enter_state()
            
            
    def render(self, display_surface):
        display_surface.fill((0, 0, 0)) # Limpa a tela
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0)) # Mostra o background
        
        temp = self.level.run(pygame.event.get()) # Recebe a display surface do Level
        display_surface.blit(temp, (0, 0)) # Desenha o Level
        temp.fill((0, 0, 0)) # Limpa o Level

