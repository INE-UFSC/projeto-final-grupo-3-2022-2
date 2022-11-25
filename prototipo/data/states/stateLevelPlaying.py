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
        self.__actions = {'esc': False, 'reset': False,
                          'up': False, 'down': False, 'left': False, 'right': False,
                          'mouse_left': False, 'mouse_right': False}
        
        self.__load_level(0)
        
    def __load_level(self, level_selected):
        current_level = config.levels[level_selected]
        self.level = Level(current_level) # Passa a matriz que representa o nível e a superfície onde o nível será desenhado
        
    def update_actions(self, event):
        if event.type == pygame.KEYDOWN: # Inputs do teclado (soltar tecla)
            if event.key == pygame.K_ESCAPE:
                self.__actions['esc'] = True
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                self.__actions['up'] = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.__actions['down'] = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.__actions['left'] = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.__actions['right'] = True
            if event.key == pygame.K_r:
                self.__actions['reset'] = True
                
        if event.type == pygame.KEYUP: # Inputs do teclado (soltar tecla)
            if event.key == pygame.K_ESCAPE:
                self.__actions['esc'] = False
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                self.__actions['up'] = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.__actions['down'] = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.__actions['left'] = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.__actions['right'] = False
            if event.key == pygame.K_r:
                self.__actions['reset'] = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Inputs do mouse (pressionar botão)
            if event.button == 1:
                self.__actions['mouse_left'] = True
            if event.button == 3:
                self.__actions['mouse_right'] = True
                    
        if event.type == pygame.MOUSEBUTTONUP: # Inputs do mouse (soltar botão)
            if event.button == 1:
                self.__actions['mouse_left'] = False
            if event.button == 3:
                self.__actions['mouse_right'] = False

    def update(self, delta_time):
        # Se o jogador pressionar ESC, entra no estado de pausa
        if self.__actions['esc']:
            pause_state = LevelPaused(self._game)
            pause_state.enter_state()
            
            
    def render(self, display_surface):
        display_surface.fill((0, 0, 0)) # Limpa a tela
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0)) # Mostra o background
        
        temp = self.level.run(pygame.event.get()) # Recebe a display surface do Level
        display_surface.blit(temp, (0, 0)) # Desenha o Level
        temp.fill((0, 0, 0)) # Limpa o Level

