import pygame
from math import pi, atan2


class Bow():
    def __init__(self):
        self.image = pygame.Surface((45, 10))
        self.image.fill('blue')
        
        
        #self.image.fill('blue')
        #self.image.set_colorkey((0,0,0))
        #self.rect = self.image.get_rect(midleft=initial_position)

    def get_rotated_image(self, player_position):
        cursor_position = pygame.mouse.get_pos()
        
        # Calcula o ângulo entre o centro do jogador e o cursor
        relative_position = pygame.Vector2(cursor_position) - pygame.Vector2(player_position)
        angle_degrees = (180 / pi) * (-atan2(relative_position[1], relative_position[0]))

        bow_image_copy = pygame.transform.rotate(self.image, angle_degrees)
        return bow_image_copy
