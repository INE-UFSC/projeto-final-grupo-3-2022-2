import os, time, pygame

from Settings import Settings
import finder

from states.abstractState import State
from states.stateTitleScreen import TitleScreen

from singletonAssets import Assets


class Game():
    def __init__(self):
        pygame.init()

        # Configurações da janela
        self.__fullscreen = False
        self.__monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.__initial_screen_width = int(self.__monitor_size[0] * 0.95)
        self.__initial_screen_height = int(self.__monitor_size[1] * 0.80)
        self.__screen = pygame.display.set_mode((self.__initial_screen_width, self.__initial_screen_height), pygame.RESIZABLE)

        pygame.display.set_caption("Speed Archer")

        # Configurações da superfície de display
        self.__display_surface = pygame.Surface((self.__initial_screen_width, self.__initial_screen_height))

        # Configurações do jogo
        self.__running, self.__playing = True, True
        self.__dt, self.__prev_time = 0, 0
        self.__clock = pygame.time.Clock()
        self.__state_stack = []

        # Carrega o jogo
        self.__load_assets() # Carrega os assets
        self.__load_states()

    def __load_assets(self):
        Assets().load_assets() # Inicializa o singleton de assets
    
    def __load_states(self):
        self.__title_screen = TitleScreen(self)
        self.__state_stack.append(self.__title_screen)

    def run(self):
        while self.__playing:
            self.__get_events()
            self.__update()
            self.__render()
            self.__get_dt()
            
            self.__clock.tick(60) # Limita o FPS

    def __get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
                self.__playing = False
            
            if event.type == pygame.VIDEORESIZE:
                self.__screen_resize()

            if event.type == pygame.KEYDOWN: # Inputs do teclado (pressionar tecla)
                if event.key == pygame.K_F11:
                    self.__fullscreen = not self.__fullscreen
                    if self.__fullscreen:
                        pygame.display.quit()
                        self.__screen = pygame.display.set_mode(self.__monitor_size, pygame.FULLSCREEN)
                        pygame.display.init()
                    else:
                        pygame.display.quit()
                        self.__screen = pygame.display.set_mode((self.__initial_screen_width, self.__initial_screen_height), pygame.RESIZABLE)
                        pygame.display.init()
                    self.__screen_resize()

            self.__update_state_actions(event)

    def __update_state_actions(self, event):
        self.__state_stack[-1].update_actions(event)

    def __update(self):
        self.__state_stack[-1].update(self.__dt)

    def __render(self):
        self.__state_stack[-1].render(self.__display_surface) # Renderiza a state atual
        self.__screen.blit(self.__display_surface, Settings.get_surface_offset())
        pygame.display.flip()

    def __get_dt(self):
        now = time.time()
        self.__dt = now - self.__prev_time
        self.__prev_time = now


    def __screen_resize(self):
        # Muda o tamanho da superfície de display
        self.__display_surface = pygame.Surface((self.__screen.get_width(), self.__screen.get_height()))
        # Notifica a classe Settings do novo tamanho da tela
        Settings.set_surface_offset(int((self.__screen.get_width() - self.__display_surface.get_width()) / 2),
                                    int((self.__screen.get_height() - self.__display_surface.get_height()) / 2))

    def reset_keys(self):
        for action in self.__actions:
            self.__actions[action] = False


    # Métodos que alteram a state stack
    def append_state(self, state: State):
        self.__state_stack.append(state)
        self.reset_keys()

    def pop_state(self):
        self.__state_stack.pop()
        self.reset_keys()


    # Getters
    @property
    def state_stack(self):
        return self.__state_stack
    @property
    def screen_width(self):
        return self.__screen.get_width()
    @property
    def screen_height(self):
        return self.__screen.get_height()
    @property
    def display_surface(self):
        return self.__display_surface
    @property
    def actions(self):
        return self.__actions
    
    # Setters
    @display_surface.setter
    def display_surface(self, display_surface):
        self.__display_surface = display_surface
