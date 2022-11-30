import pygame
from states.abstractState import State
from states.classeButton import Button
from singletons.singletonAssets import Assets


class LevelPaused(State):
    def __init__(self, game):
        ACTIONS = {'esc': False, 'mouse_left': False}

        super().__init__(game, ACTIONS)

        self.__assets = Assets()

        self.__load_buttons()

    def __load_buttons(self):
        self.CONTINUE = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), 'Continuar')
        self.LEVEL_RECORDS = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), 'Recordes do nível')
        self.EXIT_LEVEL = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), 'Voltar para o menu')

    def restart_actions(self):
        self._actions = {'esc': False, 'mouse_left': False}

    def update_actions(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._actions['esc'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self._actions['esc'] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._actions['mouse_left'] = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self._actions['mouse_left'] = False        

    def update(self, delta_time):
        """ PROBLEMA -> O botão deve ser identificado quando o mouse sobe, não quando ele está pressionado """
        if self._actions['mouse_left']:
            if self.CONTINUE.check_for_hover(pygame.mouse.get_pos()):
                self.exit_state()
            if self.LEVEL_RECORDS.check_for_hover(pygame.mouse.get_pos()):
                pass
            if self.EXIT_LEVEL.check_for_hover(pygame.mouse.get_pos()):
                while len(self._game.state_stack) > 2:
                    self._game.pop_state()

    def render(self, display_surface):
        self.CONTINUE.render(display_surface, (60, 40), 'topleft')
        self.LEVEL_RECORDS.render(display_surface, (60, 40+70), 'topleft')
        self.EXIT_LEVEL.render(display_surface, (60, 40+140), 'topleft')
