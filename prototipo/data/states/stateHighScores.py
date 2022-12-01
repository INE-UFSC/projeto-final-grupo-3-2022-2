import pygame
from states.abstractState import State
from states.classeButton import Button
from singletons.singletonAssets import Assets

from states.stateLevelPlaying import LevelPlaying
from utility.classeScoreController import ScoreController


class HighScores(State):
    def __init__(self, game):
        ACTIONS = {'mouse_left': False}

        super().__init__(game, ACTIONS)

        self.__score_controller = ScoreController()
        self.__assets = Assets()

        self.__load_buttons()
    
    def __load_buttons(self):
        self.VOLTAR = Button(self.__assets.fonts_path['text'], 35, (255, 255, 255), '< Voltar')
        self.RECORDE = Button(self.__assets.fonts_path['text'], 50, (142, 174, 222), 'Recorde')
        