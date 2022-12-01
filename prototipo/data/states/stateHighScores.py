import pygame
from states.abstractState import State
from states.classeButton import Button
from singletons.singletonAssets import Assets

from utility.classeScoreController import ScoreController


class HighScores(State):
    def __init__(self, game, background):
        ACTIONS = {'mouse_left': False}

        super().__init__(game, ACTIONS)

        self.__score_controller = ScoreController()
        self.__assets = Assets()
        self.__background = background
        self.__load_buttons()
    
    def __load_buttons(self):
        self.VOLTAR = Button(self.__assets.fonts_path['text'], 35, (255, 255, 255), '< Voltar')
        self.RANK = Button(self.__assets.fonts_path['text'], 50, (222, 142, 152), 'Rank')
        self.RECORDE = Button(self.__assets.fonts_path['text'], 50, (142, 174, 222), 'Recorde')
        self.AUTOR = Button(self.__assets.fonts_path['text'], 50, (142, 222, 160), 'Autor')
        self.SELETOR = Button(self.__assets.fonts_path['text'], 45, (222, 142, 152), '>')
        self.RANKS = []
        self.RECORDES = []
        self.AUTORES = []
        scores = self.__score_controller.get_level_scores(1)
        
        for rank in range(0, len(scores)): # Range vai depender da classe que controla os leveis
            if rank > 8:
                break
            self.RANKS.append(Button(self.__assets.fonts_path['text'], 50, (255, 255, 255), f"{rank+1}."))
            self.RECORDES.append(Button(self.__assets.fonts_path['text'], 50, (255, 255, 255), str(scores[rank][1])))
            self.AUTORES.append(Button(self.__assets.fonts_path['text'], 50, (255, 255, 255), str(scores[rank][0])))
        
    
    def update_actions(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._actions['mouse_left'] = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self._actions['mouse_left'] = False
    
    def update(self, delta_time):
        if self._actions['mouse_left']:
            if self.VOLTAR.check_for_hover(pygame.mouse.get_pos()):
                self.exit_state()
            

    def render(self, display_surface):
        background = pygame.transform.smoothscale(self.__background, (self._game.screen_width, self._game.screen_height))
        display_surface.blit(background, (0, 0))

        center = display_surface.get_rect().center
        right = display_surface.get_rect().topright

        self.VOLTAR.render(display_surface, (15, 10), position_origin = 'topleft')
        self.RANK.render(display_surface, (130, center[1] - 200))
        self.RECORDE.render(display_surface, (center[0]+50, center[1] - 200))
        self.AUTOR.render(display_surface, (right[0]-200, center[1] - 200))
        
        for i in range(0, len(self.RANKS)):
            self.RANKS[i].render(display_surface, (130, center[1] - 200 + (i + 1) * 55))
            self.RECORDES[i].render(display_surface, (center[0]+50, center[1] - 200 + (i + 1) * 55))
            self.AUTORES[i].render(display_surface, (right[0]-200, center[1] - 200 + (i + 1) * 55))
            
