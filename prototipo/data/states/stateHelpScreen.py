import pygame
from states.abstractState import State
from states.classeButton import Button
from singletonAssets import Assets
from Settings import Settings


class HelpScreen(State):
    def __init__(self, game):
        super().__init__(game)

        self.__assets = Assets()
        self.__background = self.__assets.images['background']

        self.__load_buttons()

    def __load_buttons(self):
        self.VOLTAR = Button(self.__assets.fonts_path['text'], 35, (255, 255, 255), '< Voltar')
        self.ResetLevel = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), '(R) Reset Level')
        self.Pause = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), '(ESC) Pause')
        self.Shoot = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), '(LMB) Shoot')
        self.Slow_Mo = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), '(RMB) Slow-Mo')
        self.Move = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), '(WASD and Keys Arrows) Move')
    def update(self, delta_time, actions):
        if actions['mouse_left']:
            if self.VOLTAR.check_for_hover(Settings.mouse_pos()):
                self.exit_state()

    def render(self, display_surface):
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0)) #Background

        center = display_surface.get_rect().center

        self.VOLTAR.render(display_surface, (15, 10), position_origin = 'topleft')
        self.ResetLevel.render(display_surface, (center[0]-370, center[1] - 150))
        self.Pause.render(display_surface, (center[0]-390, center[1] -30))
        self.Shoot.render(display_surface, (center[0]-390, center[1] + 90))
        self.Slow_Mo.render(display_surface, (center[0]-390, center[1] + 210))
        self.Move.render(display_surface, (center[0]+200, center[1]))
