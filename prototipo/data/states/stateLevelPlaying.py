import pygame
from random import randint # Usando para o screenshake
from states.abstractState import State
from singletonAssets import Assets
import config

from utility.staticLevelMouse import LevelMouse
from level.classeLevel import Level
from states.stateLevelPaused import LevelPaused


class LevelPlaying(State):
    def __init__(self, game):
        super().__init__(game)

        self.__actions = {'esc': False, 'restart': False,
                          'up': False, 'down': False, 'left': False, 'right': False,
                          'mouse_left': False, 'mouse_right': False}
        
        self.__assets = Assets()
        self.__buttons = pygame.sprite.Group()

        self.__screen_shake = 0
        
        self.__load_level(0)
        
    def __load_level(self, level_selected):
        current_level = config.levels[level_selected]
        self.__level = Level(current_level) # Passa a matriz que representa o nível e a superfície onde o nível será desenhado
        
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
                self.__actions['restart'] = True
                
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
                self.__actions['restart'] = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Inputs do mouse (pressionar botão)
            if event.button == 1:
                self.__actions['mouse_left'] = True
                self.__level.start_hold()
            if event.button == 3:
                self.__actions['mouse_right'] = True
                    
        if event.type == pygame.MOUSEBUTTONUP: # Inputs do mouse (soltar botão)
            if event.button == 1:
                self.__actions['mouse_left'] = False
                self.__level.end_hold()
            if event.button == 3:
                self.__actions['mouse_right'] = False

    def update(self, delta_time):
        # Se o jogador pressionar ESC, entra no estado de pausa
        if self.__actions['esc']:
            pause_state = LevelPaused(self._game)
            pause_state.enter_state()

        LevelMouse.set_offset(screen_dimensions = (self._game.screen_width, self._game.screen_height),
                                      level_dimensions = (self.__level.width, self.__level.height))

        self.__level.update(self.__actions)
 
    def render(self, display_surface):
        display_surface.fill((0, 0, 0)) # Limpa a tela

        level_surface = self.__level.render() # Recebe a display surface do level

        if self.__screen_shake > 0:
            display_surface.blit(level_surface, self.__shake(self.__screen_shake))
            self.__screen_shake -= 1
        else:
            display_surface.blit(level_surface, LevelMouse.get_offset()) # Desenha o level
        
        level_surface.fill((0, 0, 0)) # Limpa a surface do level

    def start_shake(self, duration = 3):
        self.__screen_shake = duration # Usando para shake na tela quando o jogador atira        

    def __shake(self, shake_instant):
        shake_offset = [(randint(0, 16) - 8), (randint(0, 16) - 8)]
        return shake_offset
