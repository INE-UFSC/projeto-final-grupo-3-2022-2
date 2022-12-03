import pygame
from states.abstractState import State
from utility.interface.classeTextButton import TextButton
from singletons.singletonAssets import Assets

from states.stateLevelPlaying import LevelPlaying
from utility.classeScoreController import ScoreController


class LevelSelector(State):
    def __init__(self, game, levels_list):
        ACTIONS = {'mouse_left': False}

        super().__init__(game, ACTIONS)

        self.__score_controller = ScoreController()
        self.__assets = Assets()
        self.__background = self.__assets.images['background']

        self.__levels_list = levels_list # Lista de níveis da categoria selecionada (é decidida pela tela de início, baseada no que o jogador escolheu)

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

        scores = self.__score_controller.get_all_best_scores()

        for index, level in enumerate(self.__levels_list):
            # Cria o número do nível
            self.NIVEIS.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), str(index + 1)))

            # Cria o texto com o recorde do nível e seu respectivo autor
            level_name = level['level_name']
            if level_name in scores:
                name, time = scores[level_name][0], scores[level_name][1]
            else:
                name, time = "-", "-"
            
            self.RECORDES.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), time))
            self.AUTORES.append(TextButton(self.__assets.fonts_path['text'], 50, (255, 255, 255), name))

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
                    LevelPlaying(self._game, self.__levels_list, i).enter_state()

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
