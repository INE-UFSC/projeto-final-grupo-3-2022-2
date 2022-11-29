import pygame
from states.abstractState import State


class LevelPaused(State):
    def __init__(self, game):
        super().__init__(game)

        self.__actions = {'esc': False}

    def update_actions(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__actions['esc'] = True

    def update(self, delta_time):
        if self.__actions['esc']:
            self.__actions['esc'] = False
            self.exit_state()

    def render(self, display_surface):
        display_surface.set_alpha(128)
        display_surface.fill((0, 0, 0)) # Limpa a tela
        return display_surface
