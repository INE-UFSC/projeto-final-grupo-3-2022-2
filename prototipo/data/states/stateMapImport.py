import pygame
from states.abstractState import State
from utility.interface.classeTextButton import TextButton
from singletons.singletonAssets import Assets

from states.stateLevelPlaying import LevelPlaying
from utility.classeScoreController import ScoreController

class MapImport(State):
    def __init__(self, game):
        ACTIONS = {'mouse_left': False}
        
        super().__init__(game, ACTIONS)
        
        self.__assets = Assets()
        self.__background = self.__assets.images['background']
        
        self.__load_buttons()
    
    def __load_buttons(self):
        self.VOLTAR = TextButton(self.__assets.fonts_path['text'], 35, (255, 255, 255), '< Voltar')
        self.IMPORTAR = TextButton(self.__assets.fonts_path['text'], 35, (255, 255, 255), 'Explorador de arquivos...')
        self.TEXTO_ERRO = TextButton(self.__assets.fonts_path['text'], 30, (140,140,140), '')
    
    def update_actions(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._actions['mouse_left'] = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self._actions['mouse_left'] = False
    
    def update(self, delta_time):
        if self._actions['mouse_left']:
            if self.VOLTAR.check_for_hover(pygame.mouse.get_pos()):
                self.exit_state()
            if self.IMPORTAR.check_for_hover(pygame.mouse.get_pos()):
                pass

    def render(self, display_surface):
        display_surface.fill((0, 0, 0)) # Limpa a tela
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0)) # Mostra o background

        center = display_surface.get_rect().center

        self.VOLTAR.render(display_surface, (15, 10), position_origin = 'topleft')
        self.IMPORTAR.render(display_surface, (center[0], center[1]))
        self.TEXTO_ERRO.render(display_surface, (center[0], center[1] + 60))