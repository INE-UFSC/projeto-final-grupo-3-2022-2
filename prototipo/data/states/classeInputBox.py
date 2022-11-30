import pygame

class InputBox:

    def __init__(self, font_path, font_size: int, base_color: tuple, w, h, text=''):
        self.__text = text
        self.__color = base_color
        self.__font = pygame.font.Font(font_path, font_size)
        self.__rect = pygame.Rect(300, 400, w , h)
        self.__txt_surface = self.__font.render(text, True, self.__color)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                pass
            elif event.key == pygame.K_BACKSPACE:
                self.__text = self.__text[:-1]
            else:
                self.__text += event.unicode
            # Re-render the text.
            self.__txt_surface = self.__font.render(self.__text, True, self.__color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.__txt_surface.get_width()+10)
        self.__rect.w = width

    def render(self, screen, position):
        self.__rect.center = position
        # Blit the text.
        screen.blit(self.__txt_surface, (self.__rect.x+5, self.__rect.y))
        # Blit the rect.
        pygame.draw.rect(screen, self.__color, self.__rect, 2)

    @property
    def text(self):
        return self.__text
