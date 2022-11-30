import pygame
from states.abstractState import State
from states.classeButton import Button
from states.classeInputBox import InputBox
from singletons.singletonAssets import Assets

from states.stateTitleScreen import TitleScreen


class InputName(State):
    def __init__(self, game):
        super().__init__(game)

        self.__actions = {'enter': False}
        self.__assets = Assets()
        self.__background = self.__assets.images['background']
        self.__verificador = False
        self.__load_buttons()

    def __load_buttons(self):
        self.NOME = Button(self.__assets.fonts_path['text'], 40, (255, 255, 255), 'Digite seu nome:')
        self.INPUT_BOX = InputBox(self.__assets.fonts_path['text'], 50, (255,255,255), 500)
        
        
        self.VERIFICA = Button(self.__assets.fonts_path['text'], 55, (255, 255, 255), 'Digite um nome com no mínimo 3 letras')

    def restart_actions(self):
        self.__actions = super().restart_actions(self.__actions)

    def update_actions(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(self.INPUT_BOX.text) < 3:
                    self.__verificador = True
                else:    
                    self.__actions['enter'] = True
        
        self.INPUT_BOX.update_actions(event)

    def update(self, delta_time):
        if self.__actions['enter']:
            self.__assets.user_name = str(self.INPUT_BOX.text).upper() # Salva o nome do usuário (em all caps)
            TitleScreen(self._game).enter_state()

        self.INPUT_BOX.update()
        
    def render(self, display_surface):
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0)) # Mostra o background

        center = display_surface.get_rect().center
        self.NOME.render(display_surface, (center[0], center[1] - 150))
        self.INPUT_BOX.render(display_surface, (center[0], center[1] - 50))
        if self.__verificador:
            self.VERIFICA.render(display_surface, (center[0], center[1] + 100))



