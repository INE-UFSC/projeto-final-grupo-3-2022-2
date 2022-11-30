import pygame
from random import randint # Usando para o screenshake
from states.abstractState import State
from singletons.singletonAssets import Assets
import config

from utility.staticLevelMouse import LevelMouse
from states.stateLevelPaused import LevelPaused
from level.classeLevel import Level
from utility.classeScoreController import ScoreController


class LevelPlaying(State):
    def __init__(self, game, level_atual = 0):
        ACTIONS = {'esc': False, 'restart': False,
                   'up': False, 'down': False, 'left': False, 'right': False,
                   'mouse_left': False, 'mouse_right': False}

        super().__init__(game, ACTIONS)

        self.__assets = Assets()
        self.__scoreController = ScoreController()
        self.__buttons = pygame.sprite.Group()
        self.__level_atual = level_atual
        
        self.__load_level(level_atual)
        
    def __load_level(self, level_atual):
        current_level = config.levels[level_atual]
        self.__level = Level(current_level) # Passa a matriz que representa o nível e a superfície onde o nível será desenhado
    
    def restart_actions(self):
        self._actions = {'esc': False, 'restart': False,
                          'up': False, 'down': False, 'left': False, 'right': False,
                          'mouse_left': False, 'mouse_right': False}

    def update_actions(self, event):
        if event.type == pygame.KEYDOWN: # Inputs do teclado (soltar tecla)
            if event.key == pygame.K_ESCAPE:
                self._actions['esc'] = True
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                self._actions['up'] = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self._actions['down'] = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self._actions['left'] = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self._actions['right'] = True
            if event.key == pygame.K_r:
                self._actions['restart'] = True
                
        if event.type == pygame.KEYUP: # Inputs do teclado (soltar tecla)
            if event.key == pygame.K_ESCAPE:
                self._actions['esc'] = False
            if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                self._actions['up'] = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self._actions['down'] = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self._actions['left'] = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self._actions['right'] = False
            if event.key == pygame.K_r:
                self._actions['restart'] = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Inputs do mouse (pressionar botão)
            if event.button == 1:
                self._actions['mouse_left'] = True
                self.__level.start_hold()
            if event.button == 3:
                self._actions['mouse_right'] = True
                    
        if event.type == pygame.MOUSEBUTTONUP: # Inputs do mouse (soltar botão)
            if event.button == 1:
                self._actions['mouse_left'] = False
                self.__level.end_hold()
            if event.button == 3:
                self._actions['mouse_right'] = False

    def update(self, delta_time):
        # Se o jogador pressionar ESC, entra no estado de pausa
        if self._actions['esc']:
            pause_state = LevelPaused(self._game)
            pause_state.enter_state()

        LevelMouse.set_surface_offset(screen_dimensions = (self._game.screen_width, self._game.screen_height),
                                      level_dimensions = (self.__level.width, self.__level.height))

        self.__level.update(self._actions)

        # Confere os status do nível
        if self.__level.win_status:
            self.__scoreController.add_score(self.__level_atual+1, self.__assets.user_name, 
                                                self.__level.timer.stopped_time)
            self.__next_level()
        if self.__level.restart_status:
            self.__level.restart_level()

    def __next_level(self):
        if self.__level_atual == len(config.levels):
            pass
            # Implementar fim de jogo (quando acabam os níveis)
        else:
            self.__level_atual += 1
            self.__load_level(self.__level_atual)

    def render(self, display_surface):
        display_surface.fill((0, 0, 0)) # Limpa a tela

        level_surface = self.__level.render() # Recebe a display surface do level
        level_surface = pygame.transform.scale(level_surface, (level_surface.get_width()*3, level_surface.get_height()*3))
        display_surface.blit(level_surface, (0,0)) # Desenha o level
