import pygame
from states.abstractState import State
from utility.interface.classeTextButton import TextButton
from singletons.singletonAssets import Assets
from utility.finder import find_file

from states.stateLevelSelector import LevelSelector
from states.stateHelpScreen import HelpScreen


class TitleScreen(State):
    def __init__(self, game):
        ACTIONS = {'mouse_left': False}

        super().__init__(game, ACTIONS)

        self.__assets = Assets()
        self.__background = self.__assets.images['background']
        
        self.__load_buttons()

    def __load_buttons(self):
        self.TITLE = TextButton(self.__assets.fonts_path['title'], 96, (232, 192, 50), 'Bowbound')
        self.LEVEL_SELECTOR = TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), 'Selecionar nível')
        self.CREATE_MAP = TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), 'Criar mapa')
        self.HELP = TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), 'Ajuda')

    def update_actions(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._actions['mouse_left'] = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self._actions['mouse_left'] = False

    def update(self, delta_time):
        if self._actions['mouse_left']:
            if self.LEVEL_SELECTOR.check_for_hover(pygame.mouse.get_pos()):
                LevelSelector(self._game, self.__assets.jsons['default-levels']).enter_state()
            if self.CREATE_MAP.check_for_hover(pygame.mouse.get_pos()):
                pass
            if self.HELP.check_for_hover(pygame.mouse.get_pos()):
                HelpScreen(self._game).enter_state()

    def render(self, display_surface):
        display_surface.fill((0, 0, 0)) # Limpa a tela
        
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0)) # Mostra o background

        center = display_surface.get_rect().center

        self.TITLE.render(display_surface, (center[0], center[1] - 120))
        self.LEVEL_SELECTOR.render(display_surface, (center[0], center[1]))
        self.CREATE_MAP.render(display_surface, (center[0], center[1] + 60))
        self.HELP.render(display_surface, (center[0], center[1] + 120))
