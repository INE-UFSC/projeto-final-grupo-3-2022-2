import pygame
from states.abstractState import State
from utility.interface.classeTextButton import TextButton
from singletons.singletonAssets import Assets

from states.stateLevelPlaying import LevelPlaying
from utility.classeScoreController import ScoreController


class LevelSelector(State):
    def __init__(self, game):
        ACTIONS = {'mouse_left': False}

        super().__init__(game, ACTIONS)

        self.__score_controller = ScoreController()
        self.__assets = Assets()
        self.__background = self.__assets.images['background']

        self.__load_buttons()

    def __load_buttons(self):
        self.VOLTAR = TextButton(self.__assets.fonts_path['text'], 35, (255, 255, 255), '< Voltar')
        self.NIVEL = TextButton(self.__assets.fonts_path['title'], 50, (222, 142, 152), 'Nível')
        self.RECORDE = TextButton(self.__assets.fonts_path['title'], 50, (142, 174, 222), 'Recorde')
        self.AUTOR = TextButton(self.__assets.fonts_path['title'], 50, (142, 222, 160), 'Autor')
        self.SELETOR = TextButton(self.__assets.fonts_path['text'], 45, (222, 142, 152), '>')
        self.NIVEIS = []
        self.RECORDES = []
        self.AUTORES = []
        scores = self.__score_controller.get_all_scores()
        
        for level in range(1, 9): # Range vai depender da classe que controla os leveis
            self.NIVEIS.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), str(level)))
            if level in scores:
                self.RECORDES.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), str(scores[level][0][1])))
                self.AUTORES.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), str(scores[level][0][0])))
            else:
                self.RECORDES.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), '-'))
                self.AUTORES.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), '-'))

    def update_actions(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._actions['mouse_left'] = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self._actions['mouse_left'] = False
    
    def update(self, delta_time):
        if self._actions['mouse_left']:
            if self.VOLTAR.check_for_hover(pygame.mouse.get_pos()):
                self.exit_state()
            
            for i in range(0, len(self.NIVEIS)):
                if self.NIVEIS[i].check_for_hover(pygame.mouse.get_pos()):
                    LevelPlaying(self._game, i+1).enter_state()

    def render(self, display_surface):
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0)) # Mostra o background

        center = display_surface.get_rect().center
        right = display_surface.get_rect().topright

        self.VOLTAR.render(display_surface, (15, 10), position_origin = 'topleft')
        self.NIVEL.render(display_surface, (130, center[1] - 200))
        self.RECORDE.render(display_surface, (center[0]+50, center[1] - 200))
        self.AUTOR.render(display_surface, (right[0]-200, center[1] - 200))
        
        for i in range(0, len(self.NIVEIS)):
            self.NIVEIS[i].render(display_surface, (130, center[1] - 200 + (i + 1) * 55))
            self.RECORDES[i].render(display_surface, (center[0]+50, center[1] - 200 + (i + 1) * 55))
            self.AUTORES[i].render(display_surface, (right[0]-200, center[1] - 200 + (i + 1) * 55))
            if self.NIVEIS[i].check_for_hover(pygame.mouse.get_pos()):
                self.SELETOR.render(display_surface, (100, center[1] - 200 + (i + 1) * 55))
